
  def test_lucky_months_returns_the_months_of_the_lucky_balances(self):
    self.assertEqual(lucky_months([{ "month": "January", "profit": 1001 }, { "month": "February", "profit": -10 }, { "month": "March", "profit": 2300 }, { "month": "April", "profit": 800 }]), ["January", "March"])
    
  def test_lucky_months_returns_an_empty_list_if_there_were_no_lucky_balances(self):
    self.assertEqual(lucky_months([{ "month": "January", "profit": 999 }, { "month": "February", "profit": -10 }, { "month": "March", "profit": 20 }, { "month": "April", "profit": 800 }]), [])
