
  def test_lucky_returns_balances_whose_profit_is_greater_than_1000(self):
    self.assertEqual(lucky([{ "month": "January", "profit": 1000 }, { "month": "February", "profit": 2000 }, { "month": "March", "profit": 2500 }, { "month": "April", "profit": 1001 }, { "month": "May", "profit": 0 }, { "month": "June", "profit": -25 }]), [{ "month": "February", "profit": 2000 }, { "month": "March", "profit": 2500 }, { "month": "April", "profit": 1001 }])
  
  def test_lucky_returns_an_empty_list_if_no_balance_has_profit_greater_than_1000(self):
    self.assertEqual(lucky([{ "month": "January", "profit": 1000 }, { "month": "February", "profit": 0 }, { "month": "March", "profit": 200 }, { "month": "April", "profit": -30 }]), [])