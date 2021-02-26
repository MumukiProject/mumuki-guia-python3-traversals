/*...solution[8]...*/

/*...solution[9]...*/

def promedio(lista_de_numeros):
	return sumatoria(lista_de_numeros) / len(lista_de_numeros)

def sumatoria(lista_de_numeros):
  sumatoria = 0
  for numero in lista_de_numeros:
    sumatoria = sumatoria + numero
  return sumatoria
