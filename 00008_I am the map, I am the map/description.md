Regardless of total profits or positive balances, Ana wants to get a list of all profits given a list of balances. To do this we must transform - or _map_ - each element of the list and return a new list with all those values. :thumbsup:

> Define the function `profits` which takes a list of balances and returns a list containing only the `profit` field for each one.
>
> ```python
> ムprofits([
  	{ "month": "January", "profit": 40 },
  	{ "month": "February", "profit": 12 },
  	{ "month": "March", "profit": 8}
  ])
> [40, 12, 8]
> ```