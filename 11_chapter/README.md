This is going to be the work for chapter 11 of the **Learning Test Driven Development in Python** book.

* 5 USD X 2 = 10 USD - Done in Chapter 1
* 10 EUR X 2 = 20 EUR - Done in Chapter 2
* 4002 KRW / 4 = 1000.5 KRW - Done in Chapter 2
* 5 USD + 10 USD = 15 USD - Done in Chapter 3
* Separate test code from production code - Done in Chapter 7
* Remove redundant tests - Done in Chapter 7
* 5 USD + 10 EUR = 17 USD - Done in chapter 8
* 1 USD + 1100 KRW = 2200 KRW - Done in chapter 9
* Determine exchange rate based on the currencies involved (from -> to) - Done in chapter 9
* Improve error handling when exchange rates are unspecified - Done in chapter 10
* Improve the implementation of exchange rates
* Allow exchange rates to be modified

In this chapter, we're going to focus on separating out a bank entity to take the responsibility of performing
the currency conversions.

One of the principles of DDD is continuous learning, so even though we didn't have this bank entity in our original design,
we're going to add it into our design, and use TDD to implement and validate it.

What should such a bank entity do? 
* it should hold exchange rates
* it should be able to convert money between currencies based on the exchange rate
* the banks hould allow asymmetric exchange rates
* the bank should inform us when it cannot exchange money in one currency into another because it's missing an exchange rate

Under this new design, the `Bank` will depend on `Money`, and `Portfolio` would depend on both `Bank` and `Money`.

The relationship between the `Portfolio` and `Money` abstractions is an **Aggregate** relationship from DDD.

For the dependency of `Portfolio` on `Money` and `Bank`, it's simply an interface dependency. 

**Dependency injection** is the practice of separating the initialization from the utilization of a dependent entity so that we can
write loosely coupled code.

