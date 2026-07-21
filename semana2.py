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
print(texto)

print(type(''))

### Acceso a datos
# print('texto[1] ->', texto[1])
# print('texto[-1] ->', texto[-1])

### Slicing
# print('texto[1:4] ->', texto[1:4])
# print('texto[:] ->', texto[:])
# print('texto[5:] ->', texto[5:])
# print('texto[:5] ->', texto[:5])
# print('texto[:-5] ->', texto[:-5])
# print('texto[:-5] ->', texto[:-5])
# print('texto[-5:] ->', texto[-5:])
# print('texto[-2:-5] ->', texto[-2:-5])
# print('texto[-5:-2] ->', texto[-5:-2])
# print('texto[::] ->', texto[::])
# print('texto[::2] ->', texto[::2])
# print('texto[3:-2:2] ->', texto[3:-2:2])
# print('texto[3:-2:-2] ->', texto[3:-2:-2])
# print('texto[::-1] ->', texto[::-1])

## List - Lista (Heterogeneas - Mutable)
print()
lista = [1, 'hola', 4.5, True, (False, 'ea ea'), ['soy', 'una', 'lista']]
#         0     1     2     3         4                      5           # izq -> derecha # positivos arrancando del 0 en aumento
#        -6    -5    -4    -3        -2                     -1           # derecha -> izq # negativos disminuyendo a partir del -1
print(lista)

print(type([]))

### Acceso a datos
# print('lista[1]:', lista[1])
# print('lista[-2]:', lista[-2])

### Slicing
# print('lista[1:4] ->', lista[1:4])
# print('lista[:] ->', lista[:])
# print('lista[5:] ->', lista[5:])
# print('lista[:5] ->', lista[:5])
# print('lista[:-5] ->', lista[:-5])
# print('lista[:-5] ->', lista[:-5])
# print('lista[-5:] ->', lista[-5:])
# print('lista[-2:-5] ->', lista[-2:-5])
# print('lista[-5:-2] ->', lista[-5:-2])
# print('lista[::] ->', lista[::])
# print('lista[::2] ->', lista[::2])
# print('lista[3:-2:2] ->', lista[3:-2:2])
# print('lista[3:-2:-2] ->', lista[3:-2:-2])
# print('lista[::-1] ->', lista[::-1])

### Agregar elemento
# lista.append(1400)
# print(lista)
# lista.append(True)
# print(lista)
# lista.append(['valores', 'agregados'])
# print(lista)

# lista.extend(['valores', 'agregados'])
# print(lista)

# lista.insert(1, 'me inserte en el indice 1')
# print(lista)

### Modificar elemento
# lista[0] = 'reemplace el valor que estaba al principio'
# print(lista)

# lista[:2] = (1, 2)
# print(lista)

# lista[:2] = ()
# print(lista)

# lista[:4] = []
# print(lista)

# lista[:2] = [1,2,3,4,5,6,7,8,9]
# print(lista)

# print('string a lista: ', list('hola soy pepe'))
# lista[:2] = 'hola soy pepe' -> list('hola soy pepe')
# print(lista)

### Eliminar elemento
# lista.insert(3, 'hola')
# print(lista)
# lista.remove('hola')
# print(lista)

# lista.pop()
# print(lista)
# lista.pop(3)
# print(lista)

# valor_extraido = lista.pop()
# print(lista)
# valor_extraido = lista.pop(3)
# print(lista)
# print(valor_extraido)

# lista.append(valor_extraido)
# print(lista)


## Tuple - Tupla (Heterogeneas - Inmutable)
print()
tupla = (1, 'hola', 4.5, True, [False, 'soy pepito'], ('soy', 'una', 'tupla'))
# tupla = 1, 'hola', 4.5, True
#         0     1     2     3         4                      5               # izq -> derecha # positivos arrancando del 0 en aumento
#        -6    -5    -4    -3        -2                     -1               # derecha -> izq # negativos disminuyendo a partir del -1
print(tupla)

print(type(()))

### Acceso a datos
# print('tupla[2]:', tupla[2])
# print('tupla[-4]:', tupla[-4])

### Slicing
# print('tupla[1:4] ->', tupla[1:4])
# print('tupla[:] ->', tupla[:])
# print('tupla[5:] ->', tupla[5:])
# print('tupla[:5] ->', tupla[:5])
# print('tupla[:-5] ->', tupla[:-5])
# print('tupla[:-5] ->', tupla[:-5])
# print('tupla[-5:] ->', tupla[-5:])
# print('tupla[-2:-5] ->', tupla[-2:-5])
# print('tupla[-5:-2] ->', tupla[-5:-2])
# print('tupla[::] ->', tupla[::])
# print('tupla[::2] ->', tupla[::2])
# print('tupla[3:-2:2] ->', tupla[3:-2:2])
# print('tupla[3:-2:-2] ->', tupla[3:-2:-2])
# print('tupla[::-1] ->', tupla[::-1])

## Set - Conjunto (Heterogeneos - Mutable - Solo contienen elementos inmutables)
print()
# conjunto = {1, 'hola', 4.5, True, [False, 'soy pepito'], ('soy', 'una', 'tupla'), {True, 'soy jose'}}
conjunto = {1, 'hola', 4.5, True, ('soy', 'una', 'tupla')}
print(conjunto)
print(type(set()))

### Agregar elemento
conjunto.add(False)
print(conjunto)

conjunto.update([0, 'corredor', '4.5', 4.5, ('eaea', 'test')])
print(conjunto)

### Eliminar elemento
# conjunto.remove(4.5)
# print(conjunto)
# conjunto.remove(5.5)
# print(conjunto)

# conjunto.discard(5.5)
# print(conjunto)
# conjunto.discard(4.5)
# print(conjunto)

# conjunto.pop()
# print(conjunto)
# conjunto.pop()
# print(conjunto)

# valor_extraido = conjunto.pop()
# print(conjunto)
# print(valor_extraido)


## Dict - Diccionarios
print()

# Claves/Llaves/Keys -> Solo tipo de datos inmutables
# Valores/Values -> Cualquier tipo de dato

diccionario = {
    "llave1": 1,
    "llave2": 'hola',
    True: 4.5,
    45: True,
    53.6: [False, 'soy pepito'],
    ('soy', 'la', 'llave'): ('soy', 'una', 'tupla'),
    "llave3": {True, 'soy jose'}
}
print(diccionario)
print(type({}))

### Acceso a datos
print(diccionario[53.6])
# print(diccionario['pinocho'])
print(diccionario.get(53.6))
print(diccionario.get('pinocho'))
print(diccionario.get('pinocho', 'Esa llave no existe en este diccionario'))
print(diccionario.get('pinocho', input('Ingresa vvalor por defecto a usar: ')))
print(diccionario.get(53.6, 'Esa llave no existe en este diccionario'))

### Agregar/Modificar elemento
diccionario["llave4"] = {
    'clave1': 'valor1',
    'clave2': 'valor2',
    'clave3': 'valor3',
}
print(diccionario)

diccionario[53.6] = False
print(diccionario)

diccionario.update({"llave4": 1024, "soy tu llave": 45, "llave3": {'soy solo un string en un set'}})
print(diccionario)



## Casting

# print(int('4'))
# print(float('5.67'))
# print(list((1,2,True)))
# print(tuple(['hola','don','pepito']))
# print(bool('hola'))
# set()

# print(bool(False))
# print(bool(0))
# print(bool(''))
# print(bool(0.00))
# print(bool([]))
# print(bool(()))
# print(bool(set()))
# print(bool({}))
# print(bool(None))

### len()
# print(len(texto))
# print(len(lista))
# print(len(tupla))
# print(len(conjunto))
print(len(diccionario))