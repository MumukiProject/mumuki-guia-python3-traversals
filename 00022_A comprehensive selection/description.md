Just as we can do mappings using list comprehensions, we can also use them for filtering. :raised_hands:

Let's imagine that we have the function `greater_than_5` which, given a list of numbers, returns a new list of the numbers that are... greater than 5 :stuck_out_tongue::

``` python
def greater_than_5(numbers):
  result = []
  for number in numbers:
	  if number > 5:
  		list.append(result, number)
  return result
```

Using comprehensions, we can also define this function as follows:

``` python
def greater_than_5(numbers):
  return [number for number in numbers if number > 5]
```

This comprehension is very similar to those previously discussed - it's an **expression** written between brackets that includes a mapping, an element and a sequence. However, it also has a fourth `if` section that introduces a condition - only elements that satisfy it will be actually included in the resulting list. In other words, list comprehensions can actually have four parts: 

- an element transformation;
- a name for each element in a sequence;
- a reference to a sequence;
- an optional condition.

```python
[ some_transformation(element) for element in sequence if meets_condition(element) ]
``` 

> Now it's your turn! Redefine the `lucky` function to do the same thing but using list comprehensions.