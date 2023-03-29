
  def test_positive_balances_returns_all_balances_if_they_all_have_profit_greater_than_zero(self):
    self.assertEqual(positive_balances([{ "month": "March", "profit": 10 }, { "month": "August", "profit": 2 }, { "month": "September", "profit": 8 }]), [{ "month": "March", "profit": 10 }, { "month": "August", "profit": 2 }, { "month": "September", "profit": 8 }])

  def test_positive_balances_exclude_balances_with_zero_profit(self):
    self.assertEqual(positive_balances([{ "month": "March", "profit": 10 }, { "month": "August", "profit": 2 }, { "month": "September", "profit": 0 }]), [{ "month": "March", "profit": 10 }, { "month": "August", "profit": 2 }])

  def test_positive_balances_exclude_balances_with_negative_profit(self):
    self.assertEqual(positive_balances([{ "month": "July", "profit": 12 }, { "month": "August", "profit": -2 }]), [{ "month": "July", "profit": 12 }])
 
  def test_positive_balances_returns_an_empty_list_if_all_balances_have_profit_of_zero_or_less(self):
    self.assertEqual(positive_balances([{ "month": "August", "profit": -12 }, { "month": "September", "profit": 0 }]), [])
    
    