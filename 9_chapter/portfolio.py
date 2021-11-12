from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_usd = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = 0
        for money in self.moneys:
            total += self.__convert(money, currency)
        return Money(total, currency)

    def __convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            return aMoney.amount * self._eur_to_usd
