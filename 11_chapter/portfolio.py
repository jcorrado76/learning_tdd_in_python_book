from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = 0
        failures = []
        for money in self.moneys:
            try:
                total += self.__convert(money, currency)
            except KeyError as e:
                failures.append(e)

        if len(failures) == 0:
            return Money(total, currency)
        else:
            failureMessage = ",".join(f.args[0] for f in failures)
            raise Exception(f"Missing exchange rate(s):[{failureMessage}]")

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
