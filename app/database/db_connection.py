# app/database/db_connection.py
import sqlite3
from typing import Dict, List

class DatabaseConnection:
  def __init__(self):
      self.conn = sqlite3.connect('pot_database.db')
      self.create_tables()
  
  def create_tables(self):
      cursor = self.conn.cursor()
      cursor.execute('''
          CREATE TABLE IF NOT EXISTS tools (
              id TEXT PRIMARY KEY,
              name TEXT,
              version TEXT,
              created_date TIMESTAMP,
              status TEXT,
              metadata TEXT
          )
      ''')
      self.conn.commit()
  
  def add_tool(self, tool: Dict) -> bool:
      cursor = self.conn.cursor()
      try:
          cursor.execute('''
              INSERT INTO tools (id, name, version, created_date, status)
              VALUES (?, ?, ?, ?, ?)
          ''', (tool['id'], tool['name'], tool['version'], 
               tool['created_date'], tool['status']))
          self.conn.commit()
          return True
      except Exception as e:
          print(f"Error adding tool: {e}")
          return False

  def search_tools(self, requirements: Dict) -> List[Dict]:
      cursor = self.conn.cursor()
      cursor.execute('SELECT * FROM tools')
      return [dict(zip(['id', 'name', 'version', 'created_date', 'status'], row)) 
              for row in cursor.fetchall()]