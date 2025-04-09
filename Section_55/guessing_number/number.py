class RandomNumber:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value if min_value is not None else 0
        self.max_value = max_value if max_value is not None else 100
        self.number = None
        if min_value >= max_value:
            raise ValueError("min_value must be less than max_value")

    def generate(self) -> int:
        import random
        self.number = random.randint(self.min_value, self.max_value)
        return self.number
