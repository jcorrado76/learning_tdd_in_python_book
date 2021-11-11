import unittest


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


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        self.assertEqual(tenDollars, fiveDollars.times(2))

    def testMultiplicationInEuros(self):
        ten_euros = Money(10, "EUR")
        twenty_euros = ten_euros.times(2)
        self.assertEqual(twenty_euros, Money(20, "EUR"))

    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, "KRW")

        self.assertEqual(expectedMoneyAfterDivision.amount, actualMoneyAfterDivision.amount)
        self.assertEqual(expectedMoneyAfterDivision.currency, actualMoneyAfterDivision.currency)


if __name__ == "__main__":
    unittest.main()
