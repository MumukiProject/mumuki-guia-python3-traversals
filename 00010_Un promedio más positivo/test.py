
  def test_ganancias_de_balances_positivos_devuelve_todas_las_ganancias_si_todas_son_mayores_a_cero(self):
    self.assertEqual(ganancias_de_balances_positivos([{ "mes": "enero", "ganancia": 10 }, { "mes": "febrero", "ganancia": 2 }, { "mes": "marzo", "ganancia": 5 }]), [10, 2, 5])

  def test_ganancias_de_balances_positivos_devuelve_solo_las_ganancias_que_son_mayores_a_cero(self):
    self.assertEqual(ganancias_de_balances_positivos([{ "mes": "enero", "ganancia": 10 }, { "mes": "febrero", "ganancia": -2 }, { "mes": "marzo", "ganancia": 0 }]), [10])

  def test_ganancias_de_balances_positivos_devuelve_una_lista_vacia_si_ninguna_ganancia_es_mayor_a_cero(self):
    self.assertEqual(ganancias_de_balances_positivos([{ "mes": "enero", "ganancia": -10 }, { "mes": "febrero", "ganancia": -2 }, { "mes": "marzo", "ganancia": 0 }]), [])

  def test_promedio_de_balances_positivos_devuelve_el_promedio_de_todas_las_ganancias_que_son_mayores_a_cero(self):
    self.assertEqual(promedio_de_balances_positivos([{ "mes": "enero", "ganancia": 10 }, { "mes": "febrero", "ganancia": -10 }, { "mes": "marzo", "ganancia": 2 }, { "mes": "abril", "ganancia": 0 }]), 6)