In the previous exercise we did a mapping using `for...in`. :snake: In Python there is another way to do that - _list comprehensions_! Let's look at an example of how they work. :star_struck:

If, given a list of words, we want to get a list with the lengths of each one, we can define a function like the following:

```python
def long(words):
  lengths = []
  for word in words:
	list.append(lengths, len(word))
  return lengths
```

However, we could also do it using _list comprehensions_:

``` python
def long(words):
  return [len(word) for word in words]
```

As you can see, list comprehensions are a compact way to do simple iterations. They're written between brackets and, in their simplest form, must contain at least three parts:

- an element transformation;
- a name for each element in a sequence;
- and a reference to a sequence.

```python
[ some_transformation(element) for element in sequence ]
```

⏩ Think of them as a shortcut to a mapping traversal. But the nicest thing is that comprehensions - unlike `for..in` control structure - are expressions, meaning they can be used whenever a value is expected 😮 - in a `return`, in a variable assignment, as an function invocation argument or even in the console: 

```python
ム[ 1930 + 10 * decade for decade in range(0, 10) ]
[1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
```

> Redefine the `months` function to do the same as before but using list comprehensions.