# STRINGS:

'''
Strings são sequências de caracteres
Podemos usar aspas simples ou duplas
'''

x = 'assim'
y = "Assim"

if x == y.casefold(): # == compara se as strings são iguais; = é atribuição
  print("Iguais") # casefold() e lower() converte para minúsculas

# Slicing
x = "Wagner Perin"

print(x[7:9]) # corta a string a partir do 7º caractere até o 9º
print(x[-5:])


# Converter para maiúsculas
print(x.upper())
# Converter para minúsculas
print(x.lower())
# Converter para maiúsculas e minúsculas
print(x.swapcase())

# Remover espaços em branco (início e final)
x = "   Wagner Perin   "
print(x.strip())

# Substituir caracteres
x = "Vagner Perin"
print(x.replace("V", "W")) # Não muda a variável original


nomes = "Wagner, Carlos, Andre"
alunos = nomes.split(" ") # separa a string em uma lista

print(alunos)

# Concatenação
nome = "Wagner"
sobrenome = "Perin"

nome_completo = nome + " " + sobrenome

print(nome_completo)

# Strings Formatadas
idade = 22
nome = "Wagner Perin"

saida = f"Meu nome é {nome} e tenho {idade} anos."

print(saida)


preco = 58
produto = "Vinho"

saida = f"O {produto} custa R$ {preco:.2f}"
print(saida) # :.2f define que o valor será arredondado para 2 casas decimais

# Escapes
frase = "E  o Nicolas disse \"Olá Professor!\"."

print(frase) 
# \" para imprimir aspas
# se quiser um \, basta colocar \\
# \n para pular linha