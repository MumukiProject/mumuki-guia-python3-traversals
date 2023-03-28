  
  def test_total_profit_of_first_quarter_balances_is_minus_8(self):
    self.assertEqual(total_profit([{ "month": "January", "profit": 2 }, { "month": "February", "profit": 10 }, { "month": "March", "profit": -20 }]), -8)
  
  def test_total_profit_of_last_semester_balances_is_1538(self):
    self.assertEqual(total_profit([{ "month": "July", "profit": 50 }, { "month": "August", "profit": -12 }, { "month": "September", "profit": 1000 }, { "month": "October", "profit": 300 }, { "month": "November", "profit": 200 }, { "month": "December", "profit": 0 }]), 1538)