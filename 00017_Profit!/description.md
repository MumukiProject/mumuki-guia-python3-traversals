Ana, an accountant in a well-known :office: company, has dictionaries to represent the balances for each month and various lists to store them. For example:


```python
#In July the company earned $50, in August it lost $12, etc.
last_semester_balances = [
    { "month": "July", "profit": 50 },
    { "month": "August", "profit": -12 },
    { "month": "September", "profit": 1000 },
    { "month": "October", "profit": 300 },
    { "month": "November", "profit": 200 },
    { "month": "December", "profit": 0 }
]

first_quarter_balances = [
    { "month": "January", "profit": 2 },
    { "month": "February", "profit": 10 },
    { "month": "March", "profit": -20 }
]
```

With that information, Ana needs to know the cumulative profit for a list of balances like the ones above.

> Define the function `total_profit` that, given a list of balances, returns the sum of all of them:
>
>```python
>ム total_profit(last_semester_balances)
>1538
> ```