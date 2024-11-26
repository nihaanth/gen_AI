# app/orchestrator.py
from app.agents.search_agent import SearchAgent
from app.agents.developer_agent import DeveloperAgent
from app.agents.tool_tester_agent import ToolTesterAgent
from app.agents.assigner_agent import AssignerAgent
from app.agents.tool_register_agent import ToolRegisterAgent

class AgentOrchestrator:
  def __init__(self):
      self.search_agent = SearchAgent()
      self.developer_agent = DeveloperAgent()
      self.tester_agent = ToolTesterAgent()
      self.assigner_agent = AssignerAgent()
      self.register_agent = ToolRegisterAgent()
      
  def process_query(self, query: str, query_type: str):
      if query_type == "search":
          interpreted_query = self.search_agent.interpret_query(query)
          tools = self.search_agent.search_repository(interpreted_query)
          return tools
          
      elif query_type == "develop":
          tool = self.developer_agent.create_tool({"name": query})
          test_results = self.tester_agent.test_tool(tool)
          
          if test_results["test_status"] == "passed":
              self.register_agent.register_tool(tool)
          return tool