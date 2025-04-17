from abc import ABC, abstractmethod
from typing import List, Dict, Any



class Planner(ABC):
    @abstractmethod
    def plan(self, tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        pass


class SimplePlanner(Planner):
    def __init__(self, llm_provider: str = "openai", llm_model: str = "gpt-4o-mini"):
        pass 

    def plan(self, pet_bio: dict) -> str: 
        pass 
    