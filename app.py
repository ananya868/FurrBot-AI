"""
Furrbot Chatbot API

# Endpoints:
- /ask: Ask a question to the chatbot.
- /health: Check the health of the chatbot and its components.
- /: Welcome message.
"""

import os, json, time, datetime
import asyncio
from pydantic import BaseModel, Field
from fastapi import FastAPI, Depends, HTTPException

from RAG.llm import LLM 
from RAG.db import PineconeDB
from RAG.prompt import PromptTemplate

from schemas import InputSchema, PetBioSchema


# Worker Class 
class PetChatbot: 
    def __init__(self, llm_provider: str, llm_model: str) -> None:
        # Init LLM Client 
        try:
            self.llm = LLM.init_llm(
                provider_name = llm_provider, 
                model = llm_model
            )
        except Exception as e:
            raise Exception(f"Error initializing LLM: {e}")
        
        # Init DB Client
        try:
            self.db = PineconeDB()
        except Exception as e:
            raise Exception(f"Error initializing DB: {e}")
    
    def retrieve_context(self, query: str, namespace: str, n: int = 4) -> str:
        """
        Retrieve context from the database.
        
        Args:
            query (str): The query string.
            n (int): The number of top results to return.
        
        Returns:
            str: The context string.
        """
        # Query db 
        results, _ = self.db.query(
            query = query, 
            namespace = namespace, 
            top_n = n
        )
        # Format context
        context = " ".join([i["fields"]["chunk_text"] for i in results.result.hits])
        return context
    
    def generate_answer(self, query: str, context: str, previous_conversation: list = []) -> str:
        """
        Generate an answer using the LLM.
        
        Args:
            query (str): The query string.
            context (str): The context string.
        
        Returns:
            str: The answer string.
        """
        # Build prompt 
        template = PromptTemplate()
        prompt = template.rag_prompt(
            user_query = query, 
            context = context, 
            previous_conversation = previous_conversation
        )
        # Generate answer
        answer = self.llm.generate_text(
            prompt = prompt
        )
        # Parse to dict 
        answer = json.loads(answer)
        return answer.get("answer"), answer.get("followup")


class PetChatbotFactory:
    def __init__(self):
        self.instances: dict[str, PetChatbot] = {}
        self.db = PineconeDB()
    
    def get_instance(self, llm_provider: str, llm_model: str) -> PetChatbot:
        """
        Get an instance of PetChatbot based on the LLM provider and model.

        Args:
            llm_provider (str): The LLM provider (e.g., "openai", "anthropic").
            llm_model (str): The LLM model name.

        Returns:
            PetChatbot: An instance of the PetChatbot class. 
        """
        key = f"{llm_provider}_{llm_model}"
        if key not in self.instances:
            self.instances[key] = PetChatbot(llm_provider, llm_model)
        return self.instances[key]


# Fast API app 
app = FastAPI()

chatbot_factory = None # Global Factory to manage chatbot instances
@app.on_event("startup")
async def startup_event():
    global chatbot_factory
    chatbot_factory = PetChatbotFactory()
    print("Chatbot factory initialized.")

def get_chatbot_factory():
    return chatbot_factory


# Endpoints 
@app.get("/")
async def root():
    return {"message": "Welcome to the Pet Chatbot API!"}

@app.get("/health")
async def health_check(factory: PetChatbotFactory = Depends(get_chatbot_factory)):
    # Check active instances 
    
    active_instances = list(factory.instances.keys())
    instance_count = len(factory.instances)

    # Get memory usage information 
    import psutil 
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    memory_usage_mb = memory_info.rss / 1024 / 1024  # Convert bytes to MB

    # Check Database Connection
    db_status = "healthy"
    try:
        factory.db.check_connection()
    except Exception as e:
        db_status = "unhealthy"
        print(f"Database connection error: {e}")
    
    # Check LLM Status
    llm_status = "healthy"
    try:
        # Build response
        health_data = {
            "status": "healthy",
            "timestamp": datetime.datetime.now().isoformat(),
            "uptime_seconds": int(time.time() - process.create_time()),
            "memory_usage_mb": round(memory_usage_mb, 2),
            "active_instances": instance_count,
            "instances": active_instances,
            "db_status": db_status,
            "llm_status": llm_status
        }
        return health_data
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.datetime.now().isoformat()
        }
        
@app.post("/ask")
async def chat(request: InputSchema, factory: PetChatbotFactory = Depends(get_chatbot_factory)):
    try:
        # Get chatbot instance
        chatbot = factory.get_instance(
            llm_provider = request.llm_provider,
            llm_model = request.llm_model
        )
        # Retrieve context
        context = chatbot.retrieve_context(
            query = request.question, 
            namespace = request.namespace
        )
        # Generate answer
        answer, followup = chatbot.generate_answer(
            query = request.question, 
            context = context, 
            previous_conversation = request.previous_conversation
        )
        return {"answer": answer, "followup": followup}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {e}")




        
    











