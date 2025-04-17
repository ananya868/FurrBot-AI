

class PromptTemplate:
    def __init__(self, type: str = "default"):
        self.type = type
    
    def rag_prompt(
        self, 
        user_query: str, 
        context: str,
        previous_conversation: list
    ) -> str:
        """
        Generate a prompt based on the type.
        """
        assert isinstance(user_query, str), "User query must be a string."
        assert isinstance(context, str), "Context must be a string."
        assert isinstance(previous_conversation, list), "Previous conversation must be a list."
        assert self.type in ["default"], f"Unsupported prompt type: {self.type}."

        prompt = "You are an helpful assistant, designed to assist users with their queries using a RAG system. "
        if self.type == "default":
            prompt = f"""
                You are a pet care chatbot, designed to assist users with their pet-related queries using a RAG system.
                The conversation so far is:
                {previous_conversation}

                Here is some information I retrieved that might help you answer the user's query:
                {context}
                
                User's query: {user_query}
                
                ## NOTE: 
                    - If the user is simply greeting you, then greet them back in a friendly manner, dont use the context. 
                        Otherwise, based on the conversation and the retrieved information, generate the next response.
                    - If the query is related to a previous part of the conversation, provide a follow-up response, 
                        otherwise answer using the retrieved context.
                    - Your answer should be in a friendly way, make sure to use some markdown formatting like making the important points **bold**,
                        or give point wise answer for better clearness, use emojis in most sentences to represent emotions (must do).
                    - Also generate 3 follow-up questions to keep the conversation going.

                OUTPUT FORMAT: 
                - Answer (Your response to the user)
                - Follow-up Questions (to keep the conversation going)
            """
        return prompt 