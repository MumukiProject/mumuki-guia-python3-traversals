Como podés ver todos los promedios se basan en el mismo principio :eyes:. Sumar una cantidad determinada de elementos y dividir el resultado por esa cantidad. Si quisiéramos realizar una función `promedio` genérica sería algo así:

```python
def promedio(lista_de_numeros):
	return sumatoria(lista_de_numeros) / len(lista_de_numeros)

def sumatoria(lista_de_numeros):
  sumatoria = 0
  for numero in lista_de_numeros:
    sumatoria = sumatoria + numero
  return sumatoria
```
¡Pero nosotros no tenemos una lista de números sino de diccionarios! :fearful: ¿Y entonces? :thought_balloon:
