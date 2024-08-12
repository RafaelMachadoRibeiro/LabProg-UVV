"""
def func():
  global x
  x = "Wagner"

func()

print("Meu nome é: " + x)
"""

x = "Wagner"

def func():
  global x
  x = "Carlos" 

func()

print("Meu nome é: " + x)
# vai sair o valor de Carlos pois a variável x foi declarada como global