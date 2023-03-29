Very good! :raised_hands: Now we know how to _filter_ a list. In other words, we've learned how to traverse a list and get the elements that satisfy a certain condition. In this case, we have obtained a new list with the balances that show a positive profit. :moneybag:

Filtering is also a very common traversal! It usually looks like this:

```python
def filter_something(list):
  new_list = []
  for element in list:
    if meets_condition(element):
      list.append(new_list,element)
  return new_list
```