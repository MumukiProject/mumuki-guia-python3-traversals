  
  def test_double_profits_of_balances_returns_the_double_of_the_numbers(self):
    self.assertEqual(double_profits([{ "month": "January", "profit": 1000 }, { "month": "February", "profit": -200 }, { "month": "March", "profit": 500 }]), [2000, -400, 1000])
  
  def test_double_profits_of_negative_balances_returns_a_list_of_double_negative_numbers(self):
    self.assertEqual(double_profits([{ "month": "January", "profit": -1000 }, { "month": "February", "profit": -200 }, { "month": "March", "profit": -500 }]), [-2000, -400, -1000])

  def test_double_profits_of_balances_with_zero_profit_returns_a_list_of_zeros(self):
    self.assertEqual(double_profits([{ "month": "January", "profit": 0 }, { "month": "February", "profit": 0 }]), [0, 0])