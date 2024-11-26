# app/agents/assigner_agent.py
import datetime
from typing import Dict
from app.agents.base_agent import Agent

class AssignerAgent(Agent):
  def __init__(self):
      super().__init__("Assigner Agent")
      
  def validate_tool(self, tool_id: str) -> bool:
      self.logger.log(f"Validating tool: {tool_id}")
      return True
  
  def assign_tool(self, tool_id: str, user_id: str) -> Dict:
      self.logger.log(f"Assigning tool {tool_id} to user {user_id}")
      return {
          "tool_id": tool_id,
          "user_id": user_id,
          "assigned_date": datetime.datetime.now(),
          "status": "assigned"
      }