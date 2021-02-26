
  def test_maxima_ganancia_devuelve_la_ganancia_mas_alta(self):
    self.assertEqual(maxima_ganancia([{ "mes": "enero", "ganancia": -40 }, { "mes": "febrero", "ganancia": 42 }, { "mes": "marzo", "ganancia": 19}, { "mes": "abril", "ganancia":  -5}]), 42)

  def test_maxima_ganancia_devuelve_la_ganancia_mas_alta_aun_si_son_todas_negativas(self):
    self.assertEqual(maxima_ganancia([{ "mes": "enero", "ganancia": -40 }, { "mes": "febrero", "ganancia": -13 }, { "mes": "marzo", "ganancia": -19}, { "mes": "abril", "ganancia":  -5}]), -5)

  def test_maxima_ganancia_devuelve_cero_si_el_resto_de_las_ganancias_son_negativas(self):
    self.assertEqual(maxima_ganancia([{ "mes": "enero", "ganancia": 0 }, { "mes": "febrero", "ganancia": -13 }, { "mes": "marzo", "ganancia": -19}, { "mes": "abril", "ganancia":  -5}]), 0)