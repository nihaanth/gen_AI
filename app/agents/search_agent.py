# app/agents/search_agent.py
from typing import Dict, List
from app.agents.base_agent import Agent
from app.database.db_connection import DatabaseConnection

class SearchAgent(Agent):
  def __init__(self):
      super().__init__("Search Agent")
      self.db = DatabaseConnection()
  
  def interpret_query(self, query: str) -> Dict:
      self.logger.log(f"Interpreting query: {query}")
      return {"interpreted_query": query, "requirements": []}
  
  def search_repository(self, requirements: Dict) -> List[Dict]:
      self.logger.log("Searching repository for matching tools")
      return self.db.search_tools(requirements)