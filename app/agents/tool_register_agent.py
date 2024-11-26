# app/agents/tool_register_agent.py
from typing import Dict
from app.agents.base_agent import Agent
from app.database.db_connection import DatabaseConnection

class ToolRegisterAgent(Agent):
  def __init__(self):
      super().__init__("Tool Register Agent")
      self.db = DatabaseConnection()
      
  def register_tool(self, tool: Dict) -> bool:
      self.logger.log(f"Registering tool: {tool['id']}")
      return self.db.add_tool(tool)