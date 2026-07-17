# Tipos de datos

# Enteros -> Integer -> int
2
3
0
1
-5
-45

# "Decimales" -> Flotantes -> float 
4.6
0.3
1.1
0.0
4.0
-3.4

# Complejos -> complex
4+5j
6j

# print()
# print(1)
# print(-1)
# print(-1.5)
# print(-1.5+5j)

# print(type(1))
# print(type(-1))
# print(type(-1.5))
# print(type(-1.5+5j))
# print(type(-1.5+5j).__name__)

# Cadenas de caracteres -> String -> str

'texto'
"texto"

'''texto'''
"""texto"""


# 'texto
# de pepito'
# "texto
# de pepito"

'''texto
de pepito'''
"""texto
de pepito"""

# print('texto')
# print('''texto
# de pepito''')
# print('''texto
#          de pepito''')

# print('texto\nde pep\tito')
# print('texto de pepito')
# # print('texto de 'pepito'')
# print('texto de \'pepito\'')
# print("texto de 'pepito'")

# print("texto de pepito")
# # print("texto de "pepito"")
# print("texto de \"pepito\"")
# print('texto de "pepito"')

# print('La suma de 4 + 5 da 9')
# print('La suma de 4 + 5 da 4+5')
# print(f'La suma de 4 + 5 da {4+5}')
# # print('La suma de 4 + 5 da ' + str(4+5))
# print(f'La suma de 4 + 5 da {4+5} y este resultado es del tipo {type(4+5)}')
# print('c:\casa\biancotti')
# print('c:\\casa\\biancotti')
# print(r'c:\casa\biancotti') # raw

# print('aaaaaaaaaaaaaaaaa'
#       'aaaaaaaaaaaaaaaaaa'
#       'aaaaaaaaaaaaaaaaaaaaaaaaa'
#       'aaaaaaaaaaaaaaaaaaaa'
#       'aaaaaaaaaaaaaaaaaa'
#       'aaaaaaaaaaaaaaaaaaaaaaaaaaaa'
#       'aaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
#       'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')


# pepe = (
#     'aaaaaaaaaaaaaaaaa'
#     'aaaaaaaaaaaaaaaaaa'
#     'aaaaaaaaaaaaaaaaaaaaaaaaa'
#     'aaaaaaaaaaaaaaaaaaaa'
#     'aaaaaaaaaaaaaaaaaa'
#     'aaaaaaaaaaaaaaaaaaaaaaaaaaaa'
#     'aaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
#     'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# )

# print(pepe)

# valor1 = 4
# valor2 = 5
# suma = valor1 + valor2
# print(suma)

# textoDePepe - camelCase - Js - variables y funciones
# texto_de_pepe - snake_case - Python - variables y funciones
# TextoDePepe - PascalCase - en ambos lenguajes pero para clases

# print(input('Como te llamas? ')) # siempre devuelve un string

# edad = input('Cuantos anios tenes? ')
# print(edad)
# print(edad + 5)
# print(type(edad))

# Tipos Logico - Booleanos - bool - Binario
# True
# False

# Tipos de colecciones de datos

## Strings - Cadenas de caracteres
texto = 'Este texto es un string'
#        0123456789...             # izq -> derecha # positivos arrancando del 0 en aumento
#                          ...-1   # derecha -> izq # negativos disminuyendo a partir del -1

### Acceso a datos
print(texto)
print('texto[1]:', texto[1])
print('texto[-1]:', texto[-1])

## List - Lista (Heterogeneas - Mutable)
lista = [1, 'hola', 4.5, True, (False, 'ea ea'), ['soy', 'una', 'lista']]
#         0     1     2     3         4                      5           # izq -> derecha # positivos arrancando del 0 en aumento
#        -6    -5    -4    -3        -2                     -1           # derecha -> izq # negativos disminuyendo a partir del -1

### Acceso a datos
print(lista)
print('lista[1]:', lista[1])
print('lista[-2]:', lista[-2])

## Tuple - Tupla (Heterogeneas - Inmutable)
tupla = (1, 'hola', 4.5, True, [False, 'soy pepito'], ('soy', 'una', 'tupla'))
# tupla = 1, 'hola', 4.5, True
#         0     1     2     3         4                      5               # izq -> derecha # positivos arrancando del 0 en aumento
#        -6    -5    -4    -3        -2                     -1               # derecha -> izq # negativos disminuyendo a partir del -1

### Acceso a datos
print(tupla)
print('tupla[2]:', tupla[2])
print('tupla[-4]:', tupla[-4])

## Set - Conjunto

## Dict - Diccionarios