This is going to be the work for chapter 4 of the **Learning Test Driven Development in Python** book.

* 5 USD X 2 = 10 USD - Done in Chapter 1
* 10 EUR X 2 = 20 EUR - Done in Chapter 2
* 4002 KRW / 4 = 1000.5 KRW - Done in Chapter 2
* 5 USD + 10 USD = 15 USD - Done in Chapter 3
* 5 USD + 10 EUR = 17 USD
* 1 USD + 1100 KRW = 2200 KRW

In this chapter, we're going to study the value of modularizing our code. 

**Dependency Injection** is the practice of separating the creation of an object from its usage. It increases
the cohesion of code and reduces its coupling.

Dependency injection requires different code units to be independent of each other.

One of these "independencies" is to make sure that your application code is actually independent
and separated from your unit testing code.

Now, we'll add steps to modularize our code into our task list:
* 5 USD X 2 = 10 USD - Done in Chapter 1
* 10 EUR X 2 = 20 EUR - Done in Chapter 2
* 4002 KRW / 4 = 1000.5 KRW - Done in Chapter 2
* 5 USD + 10 USD = 15 USD - Done in Chapter 3
* Separate test code from production code
* Remove redundant tests
* 5 USD + 10 EUR = 17 USD
* 1 USD + 1100 KRW = 2200 KRW


We're going to skip to chapter 7 since that's where modules in Python are discussed. Chapters 5 and 6 are for modularizing code
in Go and JavaScript, respectively. 