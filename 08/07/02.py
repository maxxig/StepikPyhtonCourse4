from datetime import datetime
class LoggerMixin:
    def log(self, level, text):
        
        print(f'{level}: {text}')