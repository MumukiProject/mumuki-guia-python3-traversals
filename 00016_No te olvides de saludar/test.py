
def test_saludar_deberia_imprimir_los_saludos_de_una_persona(self):
  out = capture_stdout(lambda: saludar(["Jorge"]))
  self.assertEqual(out, "hola Jorge\n")

def test_saludar_deberia_imprimir_los_saludos_de_dos_personas(self):
  out = capture_stdout(lambda: saludar(["Joana", "Gladys"]))
  self.assertEqual(out, "hola Joana\nhola Gladys\n")

def test_saludar_deberia_imprimir_los_saludos_de_tres_personas(self):
  out = capture_stdout(lambda: saludar(["Graciela", "Ana", "Tito"]))
  self.assertEqual(out, "hola Graciela\nhola Ana\nhola Tito\n")

def test_saludar_no_deberia_retornar_nada(self):
  self.assertTrue(saludar(["Ernesto"]) == None)