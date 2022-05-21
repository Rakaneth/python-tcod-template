from datetime import datetime

class Logger:
    """Logging utility."""

    def __init__(self, log_name: str):
        self.f = open(log_name, "a")
    
    def log(self, category: str, text: str):
        ts = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        s = f"{ts} [{category}] {text}"
        self.f.write(s)
    
    def __del__(self):
        self.f.close()


LOGGER = Logger("more-tcod.log")