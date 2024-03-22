from time import perf_counter
class AdvancedTimer:
    def __init__(self):
        self.last_run, self.min, self.max = None, None, None
        self.runs = []
    def __enter__(self):
        self.start = perf_counter()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        res = perf_counter() - self.start
        self.last_run = res
        self.runs.append(res)
        if self.max is None or res >= self.max:
            self.max = res
        if self.min is None or res <= self.min:
            self.min = res

