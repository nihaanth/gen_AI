# app/agents/base_agent.py
from app.utils.logger import Logger

class Agent:
  def __init__(self, name: str):
      self.name = name
      self.logger = Logger()