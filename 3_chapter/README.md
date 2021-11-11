This is going to be the work for chapter 2 of the **Learning Test Driven Development in Python** book.

We've copied our list of features from chapter 1 so we can continue working on them here. 

* 5 USD X 2 = 10 USD - Done in Chapter 1
* 10 EUR X 2 = 20 EUR
* 4002 KRW / 4 = 1000.5 KRW
* 5 USD + 10 EUR = 17 USD
* 1 USD + 1100 KRW = 2200 KRW


We're going to start with working on the second feature in this chapter. 

We are also going to work on the third feature in this chapter, division.

When comparing equality in our tests, we can toy with implementing the `__eq__` method for our classes.

By default, equality in python is done by reference: two objects are equal if they point to the same object.
This is a very strict definition of equality - it means that an object is **only** equal to itself, not any other object,
even if they have the same state. 

Equality is determined by reference, not by value by default.

So, we just need to explicitly override the `__eq__` method.