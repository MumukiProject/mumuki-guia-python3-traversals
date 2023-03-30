
  def test_positive_balances_count_of_a_list_with_one_positive_balance_is_one(self):
    self.assertEqual(positive_balances_count([{ "month": "November", "profit": 5 }]), 1)

  def test_positive_balances_count_of_a_list_with_two_positive_balances_is_two(self):
    self.assertEqual(positive_balances_count([{ "month": "March", "profit": 8 }, { "month": "August", "profit": 10 }]), 2)

  def test_positive_balances_count_an_empty_list_is_zero(self):
    self.assertEqual(positive_balances_count([]), 0)

  def test_positive_balances_count_when_all_balances_had_zero_profit_is_zero(self):
    self.assertEqual(positive_balances_count([{ "month": "March", "profit": 0 }, { "month": "August", "profit": 0 }]), 0)

  def test_positive_balances_count_with_three_positive_balances_and_one_negative_is_three(self):
    self.assertEqual(positive_balances_count([{ "month": "January", "profit": 10 }, { "month": "February", "profit": -14 }, { "month": "March", "profit": 2 }, { "month": "April", "profit": 100 }]), 3)
  
  def test_positive_balances_count_when_all_balances_had_negative_profit_is_zero(self):
    self.assertEqual(positive_balances_count([{ "month": "January", "profit": -1 }, { "month": "February", "profit": -2 }, { "month": "March", "profit": -3 }]), 0)
