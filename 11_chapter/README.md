This is going to be the work for chapter 10 of the **Learning Test Driven Development in Python** book.

* 5 USD X 2 = 10 USD - Done in Chapter 1
* 10 EUR X 2 = 20 EUR - Done in Chapter 2
* 4002 KRW / 4 = 1000.5 KRW - Done in Chapter 2
* 5 USD + 10 USD = 15 USD - Done in Chapter 3
* Separate test code from production code - Done in Chapter 7
* Remove redundant tests - Done in Chapter 7
* 5 USD + 10 EUR = 17 USD - Done in chapter 8
* 1 USD + 1100 KRW = 2200 KRW - Done in chapter 9
* Determine exchange rate based on the currencies involved (from -> to) - Done in chapter 9
* Improve error handling when exchange rates are unspecified
* Allow exchange rates to be modified

We want to be able to handle errors better within our application.

We want to be able to:
* raise an error when a necessary currency is missing
* the error should list **all** missing exchange rates that prevent a portfolio from being evaluated, not just the first one
* when an error is returned, you should not return a valid `Money` object

In this chapter, we improved the error handling by our code by emitting a custom message, and creating a unit test
that checks for that exact message to be emitted when a missing currency exchange rate is encountered.