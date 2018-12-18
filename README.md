# Cooking with Python

This project introduces the major concepts of the Python programming language
in one exercise that keeps building on itself.

Watch the associated video walkthrough on youtube here:

## Part 1: Soup 🍜

### Your task

Create a `Soup` object that takes as input a list of `Ingredient` objects.

Every `Soup` instance should have a class method called `cook()` that prepares the soup.

After calling `cook()` on a new soup instance, the object should contain the following information:

* name of the soup (e.g. a mix of all the names of the `Ingredient`s passed)
* an attribute called `serves` that shows a number of people that will get full from this soup
(make up some calculation on how to define this)
* a custom `__str__()` method that prints out e.g. an ASCII-art soup, or some informative text about the `Soup`

Have fun!