# app/utils/logger.py
import datetime

class Logger:
  def log(self, message: str):
      print(f"[{datetime.datetime.now()}] {message}")