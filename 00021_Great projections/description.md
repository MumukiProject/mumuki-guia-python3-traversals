Ana makes a lot of projections using her company's balances. Now that we know how to do mappings, we are ready to help her with this special request: _"We need to calculate the profits of the balances as if they were all doubled"_ :moneybag:. For example:

``` python
ム last_semester_balances = [
    { "month": "july", "profit": 50 },
    { "month": "august", "profit": -12 },
    { "month": "september", "profit": 1000 },
    { "month": "october", "profit": 300 },
    { "month": "november", "profit": 200 },
    { "month": "december", "profit": 0 }
]

ム double_profits(last_semester_balances)
[100, -24, 2000, 600, 400, 0]
```

As you can see, if the profit was negative now it will be double negative! :chart_with_downwards_trend:

> Define the function `double_profits`. You can use both `for...in` and list comprehensions, whatever you prefer. :relaxed: