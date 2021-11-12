import unittest
from money import Money
from portfolio import Portfolio


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        ten_euros = Money(10, "EUR")
        twenty_euros = ten_euros.times(2)
        self.assertEqual(twenty_euros, Money(20, "EUR"))

    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, "KRW")

        self.assertEqual(expectedMoneyAfterDivision.amount, actualMoneyAfterDivision.amount)
        self.assertEqual(expectedMoneyAfterDivision.currency, actualMoneyAfterDivision.currency)

    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))

    def test_adding_dollars_and_euros(self):
        five_dollars = Money(5, "USD")
        ten_euros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_euros)
        expected_value = Money(17, "USD")
        actual_value = portfolio.evaluate("USD")
        self.assertEqual(expected_value, actual_value, f"{expected_value} != {actual_value}")

    def test_addition_of_dollars_and_wons(self):
        one_dollar = Money(1, "USD")
        eleven_hundred_won = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar, eleven_hundred_won)
        expected_value = Money(2200, "KRW")
        actual_value = portfolio.evaluate("KRW")
        self.assertEqual(expected_value, actual_value, f"{expected_value} != {actual_value}")

    def test_addition_with_multiple_missing_exchange_rates(self):
        one_dollar = Money(1, "USD")
        one_euro = Money(1, "EUR")
        one_won = Money(1, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar, one_euro, one_won)
        with self.assertRaisesRegex(Exception, "Missing exchange rate\(s\):\[USD\->Kalganid,EUR->Kalganid,KRW->Kalganid]"):
            portfolio.evaluate("Kalganid")


if __name__ == "__main__":
    unittest.main()
