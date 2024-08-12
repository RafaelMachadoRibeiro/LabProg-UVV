# BOOLEAN (True, False)
print(10 > 9)

'''
OPERADORES:
- Aritméticos: +, -, *, /, %, //, **
- Atribuição: =, +=, -=, *=, /=, %=, //=, **=
- Comparação: ==, !=, >, <, >=, <=
- Lógicos: and, or, not
- Membro: in, not in

- Identidade: is, is not
'''

a = 10
b = 3

c = a % b # resto da divisão
c = a ** b # potência (elevado)
c = a / b # divisão
c = a // b # divisão inteira

print(c)


# ATRIBUIÇÕES:
x = 3

x += 3 # x = (x + 3)
x -= 4 # x = (x - 3)
x *= 4 # x = (x * 3)
x /= 4 # x = (x / 3)
# etc.

print(x)

# COMPARAÇÕES:
'''
==   ->  igual a
!=   ->  diferente de
>    ->  maior que
<    ->  menor que
>=   ->  maior ou igual a
<=   ->  menor ou igual a
'''

# LÓGICOS:
'''
and  ->  e
or   ->  ou
not  ->  não
'''
a = 20 > 5 and 5 < 8
print(a)


# MEMBRO:
'''
in     ->  contém
not in ->  não contém
'''
alunos = ['Carlos', 'Andre', 'Joao']

print('Carlos' in alunos) # vai imprimir True pois o nome está na lista