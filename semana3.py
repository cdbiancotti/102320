# Semana 3 - Condicionales y Iteraciones

## Operadores

### Aritmeticos

#### Suma
suma = 2 + 2

#### Resta
resta = 2 - 2

#### Multiplicacion
multiplicacion = 2 * 2

#### Potencia
potencia = 2 ** 2

#### Division
division = 2 / 2

#### Division Entera
division_entera = 2 // 2

#### Modulo
modulo = 2 % 2

print('Operadores Aritmenticos')
print()
print("Suma 2 + 2 ->", suma)
print("Resta 2 - 2 ->", resta)
print("Multiplicacion 2 * 2 ->", multiplicacion)
print("Potencia 2 ** 2 ->", potencia)
print("Division 2 / 2 ->", division)
print("Division Entera 2 // 2 ->", division_entera)
print("Modulo 2 % 2 ->", modulo)
print()
print("2.0 // 2 ->", 2.0 // 2)
print("2 // 2.0 ->", 2 // 2.0)
print("2.0 % 2 ->", 2.0 % 2)
print("2 % 2.0 ->", 2 % 2.0 )
print()
print()


### Relacionales

#### Mayor que
mayor_que = 2 > 2

#### Mayor igual que
mayor_igual_que = 2 >= 2 # > = -> >=

#### Menor que
menor_que = 2 < 2

#### Menor igual que
menor_igual_que = 2 <= 2 # < = -> <=

#### Igualdad
igualdad = 2 == 2

#### Desigualdad
desigualdad = 2 != 2 # ! = -> !=

# =======================================================
# > Nota
# Tipo logicos/booleanos/binarios
# Boolean -> bool
# True - False
# =======================================================
print('Operadores Relacionales')
print()
print("Mayor que 2 > 2 ->", mayor_que)
print("Mayor igual que 2 >= 2 ->", mayor_igual_que)
print("Menor que 2 < 2 ->", menor_que)
print("Menor igual que 2 <= 2 ->", menor_igual_que)
print("Igualdad 2 == 2 ->", igualdad)
print("Desigualdad 2 != 2 ->", desigualdad)
print()
# =======================================================
# > Nota
# Valores de caracteres
# ASCII - https://elcodigoascii.com.ar/
# Unicode - https://symbl.cc/es/unicode-table/
# ord()
# print('Ordinal de "a":', ord('a'))
# chr()
# print('Caracter con ordinal 97:', chr(97))
# =======================================================

print("'a' > 'A' ->", 'a' > 'A')
print("'pepe' > 'ricardo' ->", 'pepe' > 'ricardo')
print("'pepe' > 'peperdo' ->", 'pepe' > 'peperdo')
print("'pepe' > 'pePerdo' ->", 'pepe' > 'pePerdo')
print()
print()


### Logicos


#### and (en js es &&)
 
# nombre_de_usuario = 'pepe'
# documento = 200000

# nombre_de_usuario > 'p' and documento % 4 == 0

# operacion and operacion
#    True   and   True    -> True
#    False  and   True    -> False
#    True   and   False   -> False
#    False  and   False   -> False

# 4/0
# True and 4/0
# 4/0 and True
# 4/0 and False
# False and 4/0
# variable = False
# 5 < 1 and 4/0


#### or (en js es ||)
# nombre_de_usuario = 'pepe'
# documento = 200000

# nombre_de_usuario > 'p' or documento % 4 == 0

# operacion or operacion
#    True   or   True    -> True
#    False  or   True    -> True
#    True   or   False   -> True
#    False  or   False   -> False

# 4/0
# True or 4/0
# 4/0 or True
# 4/0 or False
# False or 4/0

#### not (en js es !)
# nombre_de_usuario = 'pepe'

# not nombre_de_usuario

# not valor
#   True     -> False
#   False    -> True

# ===============================================================
# ===============================================================
# ===============================================================

# temperatura = float(input('Cual es la temperatura actual? '))

# # if condicion:
# #     codigo

# if temperatura < 8:
#     print('Que frio!!')

# # if temperatura < 25 and temperatura > 20:
# # if temperatura > 20 and temperatura < 25:
# if 20 < temperatura < 25:
#     print('Que buen clima!')
# else:
#     print('Ingresaste un valor que no esta catalogado...')


# ===============================================================
# ===============================================================

# temperatura = float(input('Cual es la temperatura actual? '))

# if temperatura < 8:
#     print('Que frio!!')
# elif 20 < temperatura < 25:
#     print('Que buen clima!')
# else:
#     print('Ingresaste un valor que no esta catalogado...')
# ===============================================================
# ===============================================================
temperatura = float(input('Cual es la temperatura actual? '))

if temperatura < 8:
    print('Que frio!!')
elif 20 < temperatura < 25:
    print('Que buen clima!')
elif 36 < temperatura < 41:
    print('Apagame la hornalla!')

# ===============================================================
# ===============================================================
temperatura = float(input('Cual es la temperatura actual? '))

if temperatura < 8:
    print('Que frio!!')
elif 20 < temperatura < 25:
    print('Que buen clima!')
elif 36 < temperatura < 41:
    print('Apagame la hornalla!')
elif 9 < temperatura < 17:
    # pass
    ...
else:
    print('Ingresaste un valor que no esta catalogado...')

# variable_a_usar = pass
# variable_a_usar = ...
# ===============================================================
# ===============================================================
