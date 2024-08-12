print('Informe o valor do A: ')
a = int(input())
print('Informe o valor do B: ')
b = int(input())
print('Informe o valor do C: ')
c = int(input())
"""
if a > b:
  print('Mensagem 1')
print('Mensagem 2')
"""
# Msg.2 não está no if pelo posicionamento (funcionou como um else)

if a > b:
  print('Mensagem 1')
if a > c:
  print('Mensagem 2')
  print('Mensagem 3')
print('Mensagem 4')
