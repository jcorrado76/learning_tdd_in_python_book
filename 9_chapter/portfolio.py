from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = 0
        for money in self.moneys:
            total += self.__convert(money, currency)
        return Money(total, currency)

    def __convert(self, aMoney, aCurrency):
        exchange_rates = {
            "EUR->USD": 1.2,
            "USD->KRW": 1100
        }
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            key = f"{aMoney.currency}->{aCurrency}"
            return aMoney.amount * exchange_rates[key]
