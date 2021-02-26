
  def test_minima_ganancia_positiva_devuelve_la_ganancia_mas_baja_de_las_positivas(self):
    self.assertEqual(minima_ganancia_positiva([{ "mes": "enero", "ganancia": -40 }, { "mes": "febrero", "ganancia": 42 }, { "mes": "marzo", "ganancia": 19}, { "mes": "abril", "ganancia":  -5}]), 19)

  def test_minima_ganancia_positiva_devuelve_la_unica_ganancia_positiva_si_solo_tiene_una(self):
    self.assertEqual(minima_ganancia_positiva([{ "mes": "enero", "ganancia": -40 }, { "mes": "febrero", "ganancia": 42 }, { "mes": "marzo", "ganancia": -19}, { "mes": "abril", "ganancia":  -5}]), 42)