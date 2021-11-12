This is going to be the work for chapter 9 of the **Learning Test Driven Development in Python** book.

* 5 USD X 2 = 10 USD - Done in Chapter 1
* 10 EUR X 2 = 20 EUR - Done in Chapter 2
* 4002 KRW / 4 = 1000.5 KRW - Done in Chapter 2
* 5 USD + 10 USD = 15 USD - Done in Chapter 3
* Separate test code from production code - Done in Chapter 7
* Remove redundant tests - Done in Chapter 7
* 5 USD + 10 EUR = 17 USD - Done in chapter 8
* 1 USD + 1100 KRW = 2200 KRW
* Determine exchange rate based on the currencies involved (from -> to)
* Improve error handling when exchange rates are unspecified
* Allow exchange rates to be modified

In this chapter, we essentially used a dictionary that was hard coded into our `__convert` method to store
the exchange rates between multiple currencies, and we reference it when we're trying to add two
`Money` objects with different currencies together.

In addition, we want to add better error handling when we are using currencies that aren't supported by our 
code.