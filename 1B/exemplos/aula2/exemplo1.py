# ESCOPO DE VARÁVEIS:

# Ex.: Global
x = "Pedro"

def func():
  x = "Carlos"
  print("Meu nome é: " + x)

def func2():
  print("Meu nome é: " + x)

func()
func2()

print("Meu nome é: " + x")