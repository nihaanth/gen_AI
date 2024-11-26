# run.py
from flask import Flask, render_template, request, jsonify
from app.orchestrator import AgentOrchestrator

app = Flask(__name__)
orchestrator = AgentOrchestrator()

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search_tools():
  query = request.json.get('query')
  results = orchestrator.process_query(query, "search")
  return jsonify(results)

@app.route('/api/create_tool', methods=['POST'])
def create_tool():
  tool_data = request.json
  new_tool = orchestrator.process_query(tool_data['name'], "develop")
  return jsonify(new_tool)

if __name__ == '__main__':
  app.run(debug=True)