
  def test_long_month_balances_of_the_first_semester_returns_the_balances_of_january_march_and_may(self):
    self.assertEqual(long_month_balances([{ "month": "January", "profit": 1000 }, { "month": "February", "profit": -200 }, { "month": "March", "profit": 500 }, { "month": "April", "profit": 800 }, { "month": "May", "profit": 770 }, { "month": "June", "profit": 870 }]), [{ "month": "January", "profit": 1000 }, { "month": "March", "profit": 500 }, { "month": "May", "profit": 770 }])

  def test_long_month_balances_of_the_last_semester_returns_the_balances_of_july_august_october_and_december(self):
    self.assertEqual(long_month_balances([{ "month": "July", "profit": 500 }, { "month": "August", "profit": 900 }, { "month": "September", "profit": 1800 }, { "month": "October", "profit": 900 }, { "month": "November", "profit": 2300 }, { "month": "December", "profit": 2000 }]), [{ "month": "July", "profit": 500 }, { "month": "August", "profit": 900 }, { "month": "October", "profit": 900 }, { "month": "December", "profit": 2000 }])

  def test_long_month_balances_of_the_first_quarter_returns_the_balances_of_january_and_march(self):
    self.assertEqual(long_month_balances([{ "month": "January", "profit": 1000 }, { "month": "February", "profit": -200 }, { "month": "March", "profit": 500 }]), [{ "month": "January", "profit": 1000 }, { "month": "March", "profit": 500 }])

  def test_long_month_balances_of_the_second_quarter_returns_the_balance_of_may(self):
    self.assertEqual(long_month_balances([{ "month": "April", "profit": 800 }, { "month": "May", "profit": 770 }, { "month": "June", "profit": 870 }]), [{ "month": "May", "profit": 770 }])
