En el ejercicio anterior hicimos un mapeo utilizando `for...in`. En Python contamos con otras formas de hacer eso, ¡las listas por comprensión! :star_struck:

Veamos cómo funcionan, si por ejemplo tuviesemos una lista de strings...

``` python
ム palabras = ["mapeo", "por", "comprensión"]
```

... y quisieramos obtener una lista con los largos de cada string, podríamos escribir:

``` python
ム [len(palabra) for palabra in palabras]
[5, 3, 11]
```

> Redefiní la función `meses` para que haga lo mismo que antes pero utilizando listas por comprensión. 