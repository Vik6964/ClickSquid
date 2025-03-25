import sys
from datetime import datetime
from .line import Line
from .db import DB

class ClickSquid:
    def __init__(self, config, error_file_path):
        self.input = sys.stdin
        self.client = DB(config)
        self.error_file_path = error_file_path
        
    def run(self):
        for string in self.input:
            log_line = Line(string)
            if log_line.valid():
                try:
                    self.client.insert(log_line.line)
                except Exception as e:
                    with open(self.error_file_path, 'a') as error_file:
                        error_file.write(f"{log_line.line}\n")
                        error_file.write(f"{e}\n")
