
  def test_months_of_a_quarter_returns_three_months(self):
    self.assertEqual(months([{ "month": "January", "profit": 10 }, { "month": "February", "profit": 2 }, { "month": "March", "profit": 5 }]), ["January", "February", "March"])
  
  def test_months_of_a_semonthter_returns_six_months(self):
    self.assertEqual(months([{ "month": "January", "profit": 10 }, { "month": "February", "profit": 2 }, { "month": "March", "profit": 5 }, { "month": "April", "profit": 8 }, { "month": "May", "profit": 12 }, { "month": "June", "profit": 25 }]), ["January", "February", "March", "April", "May", "June"])