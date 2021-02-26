
  def test_ganancia_promedio_con_dos_balances_suma_la_ganancia_de_ambos_y_divide_por_dos(self):
    self.assertEqual(ganancia_promedio([{ "mes": "marzo", "ganancia": 30 }, { "mes": "agosto", "ganancia": 10 }]), 20)

  def test_ganancia_promedio_con_tres_balances_suma_la_ganancia_de_los_tres_y_divide_por_tres(self):
    self.assertEqual(ganancia_promedio([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": 9 }]), 7)
