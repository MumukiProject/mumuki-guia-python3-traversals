
  def test_profits_of_three_months_balances_returns_only_three_profits(self):
    self.assertEqual(profits([{ "month": "March", "profit": 10 }, { "month": "August", "profit": 2 }, { "month": "September", "profit":0 }]), [10, 2, 0])

  def test_profits_of_four_months_balances_returns_only_four_profits(self):
    self.assertEqual(profits([{ "month": "March", "profit": 10 }, { "month": "August", "profit": 2 }, { "month": "September", "profit":0 }, { "month": "December", "profit": 8 }]), [10, 2, 0, 8])

  def test_profits_of_two_months_balances_returns_only_two_profits(self):
    self.assertEqual(profits([{ "month": "March", "profit": 8 }, { "month": "August", "profit": 7 }]), [8,7])
