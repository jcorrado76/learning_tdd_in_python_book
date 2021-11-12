class Money:
    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier: float):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor: float):
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __str__(self):
        return f"({self.currency}, {self.amount:0.2f})"
