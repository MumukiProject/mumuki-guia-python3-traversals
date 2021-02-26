
  def test_meses_devuelve_los_meses_de_los_balances_de_un_trimestre(self):
    self.assertEqual(meses([{ "mes": "enero", "ganancia": 10 }, { "mes": "febrero", "ganancia": 2 }, { "mes": "marzo", "ganancia": 5 }]), ["enero", "febrero", "marzo"])
  
  def test_meses_devuelve_los_meses_de_los_balances_de_un_semestre(self):
    self.assertEqual(meses([{ "mes": "enero", "ganancia": 10 }, { "mes": "febrero", "ganancia": 2 }, { "mes": "marzo", "ganancia": 5 }, { "mes": "abril", "ganancia": 8 }, { "mes": "mayo", "ganancia": 12 }, { "mes": "junio", "ganancia": 25 }]), ["enero", "febrero", "marzo", "abril", "mayo", "junio"])
  
  def test_afortunados_devuelve_los_balances_cuya_ganancia_es_mayor_a_1000(self):
    self.assertEqual(afortunados([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": 2000 }, { "mes": "marzo", "ganancia": 2500 }, { "mes": "abril", "ganancia": 1001 }, { "mes": "mayo", "ganancia": 0 }, { "mes": "junio", "ganancia": -25 }]), [{ "mes": "febrero", "ganancia": 2000 }, { "mes": "marzo", "ganancia": 2500 }, { "mes": "abril", "ganancia": 1001 }])
  
  def test_afortunados_devuelve_una_lista_vacia_si_ningun_balance_tiene_ganancia_mayor_a_1000(self):
    self.assertEqual(afortunados([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": 0 }, { "mes": "marzo", "ganancia": 200 }, { "mes": "abril", "ganancia": -30 }]), [])
  
  def test_meses_afortunados_devuelve_los_meses_cuyos_balances_son_mayores_a_1000(self):
    self.assertEqual(meses_afortunados([{ "mes": "enero", "ganancia": 1001 }, { "mes": "febrero", "ganancia": -10 }, { "mes": "marzo", "ganancia": 2300 }, { "mes": "abril", "ganancia": 800 }]), ["enero", "marzo"])