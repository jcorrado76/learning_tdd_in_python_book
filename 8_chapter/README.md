This is going to be the work for chapter 8 of the **Learning Test Driven Development in Python** book.

* 5 USD X 2 = 10 USD - Done in Chapter 1
* 10 EUR X 2 = 20 EUR - Done in Chapter 2
* 4002 KRW / 4 = 1000.5 KRW - Done in Chapter 2
* 5 USD + 10 USD = 15 USD - Done in Chapter 3
* Separate test code from production code - Done in Chapter 7
* Remove redundant tests - Done in Chapter 7
* 5 USD + 10 EUR = 17 USD
* 1 USD + 1100 KRW = 2200 KRW

In this chapter, we'll work on dealing with mixed currencies.

There are a few requirements relating how conversion happens:
* conversion always relates a pair of currencies
* conversion from one currency to another occurs with a well-defined exchange rate
* the exchange rate between two currencies may or may not be arithmetic reciprocals
* it is possible for a currency to have no defined exchange rate to another currency

We will use TDD to implement each one of these properties at a time.

After implementing the features for converting one currency to another when we want to evaluate them and 
add them together, we realize that we need some additional features, which we can add to this list.

This is one additional benefit of TDD: you can more easily determine and add tasks/features where appropriate
in your planning.

In this case, we need to add tasks to determine the exchange rate based on the currencies involved, and
we need to add functionality that allows exchange rates to be modified.

This results in the following updated plan:
* 5 USD X 2 = 10 USD - Done in Chapter 1
* 10 EUR X 2 = 20 EUR - Done in Chapter 2
* 4002 KRW / 4 = 1000.5 KRW - Done in Chapter 2
* 5 USD + 10 USD = 15 USD - Done in Chapter 3
* Separate test code from production code - Done in Chapter 7
* Remove redundant tests - Done in Chapter 7
* 5 USD + 10 EUR = 17 USD
* 1 USD + 1100 KRW = 2200 KRW
* Determine exchange rate based on the currencies involved (from -> to)
* Allow exchange rates to be modified