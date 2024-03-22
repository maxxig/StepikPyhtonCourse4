class Suppress:
    def __init__(self, *args):
        self._args = args
        self.exception = None
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self._args:
            self.exception = exc_val
            return True
        return False