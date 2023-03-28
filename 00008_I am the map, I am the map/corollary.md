Excellent! :clap: Now we know how to transform each element of a list to get a new list :muscle:. This operation is very common and is called _mapping_ a list. Mappings are _traversals_ that usually have the following structure: 

```python
def map_something(list):
	new_list = []
	for element in list:
    list.append(new_list, some_transformation(element))
  return new_list
```
