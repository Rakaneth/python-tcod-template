from datetime import datetime

class Logger:
    """Logging utility."""

    def __init__(self, log_name: str):
        print(f"Opening log file {log_name}")
        self.f = open(log_name, "a")
    
    def log(self, category: str, text: str):
        ts = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        s = f"{ts} [{category}] {text}"
        self.f.write(s)
    
    def __del__(self):
        print(f"Closing log file {self.f.name}")
        self.f.close()


LOGGER = Logger("more-tcod.log")