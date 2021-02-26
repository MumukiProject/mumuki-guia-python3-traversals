
  def test_promedio_ganancias_positivas_con_dos_balances_positivos_y_uno_negativo_da_la_suma_de_ganancias_mayores_a_cero_dividida_por_dos(self):
    self.assertEqual(promedio_ganancias_positivas([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": -9 }]), 6)
  
  def test_promedio_ganancias_positivas_con_dos_balances_positivos_y_uno_negativo_da_la_suma_de_ganancias_mayores_a_cero_divida_por_dos(self):
    self.assertEqual(ganancia_positiva([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": -9 }]), 12)

  def test_promedio_ganancias_positivas_con_un_balance_positivo_un_balance_con_ganancia_cero_y_uno_negativo_da_la_ganancia_mayor_a_cero(self):
    self.assertEqual(ganancia_positiva([{ "mes": "marzo", "ganancia": 0 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": -9 }]), 2)