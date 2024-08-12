"""
VARIÁVEIS
"""

x = 10
y = 10.5

a = '25'
"b = a * x"  # não está implicito que é um nº então irá repetir o nº 25 10 vezes
b = int(a) * x  # variável explícita
c = a * x

print(b)
print(c)

d = a + str(x)
print(d)
