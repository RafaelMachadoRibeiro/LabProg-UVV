"""
LISTAS:
 - Uma lista é uma sequência de elementos.
 - Podemos criar uma lista vazia com []
 - Podemos criar uma lista com elementos separados por vírgula
 - Podemos criar uma lista com elementos de outra lista

Características:
 - Ordenadas
 - Indexadas (recebem índices, começando em 0)
 - Mutável/modificáveis (podemos alterar os elementos)
 - Permite duplicatas (elementos podem aparecer mais de uma vez)
"""

# Exemplo 1 de lista (strings):
nomes = ["Wagner", "Antonio", "Jose", "Joao"] 
print(nomes)

nomes[2] = "Maria" # Altera o elemento na posição 2

print(nomes[2]) # imprime o 3º elemento da lista
print(nomes[2:]) # imprime os elementos da lista a partir do 3º
print(nomes[2:4]) # imprime os elementos da lista do 3º até o 4º
print(nomes[-1]) # imprime o último elemento da lista

print(len(nomes)) # imprime o tamanho da lista

print(type(nomes)) # imprime o tipo da lista
print(type(nomes[2])) # imprime o tipo do 3º elemento da lista


# Exemplo 2 de lista:
dados = ["Nicolas" 20, 1.86, True]
print(dados)


# in operator
if "Maria" in nomes:
  print('Eu conheço a Maria!')
else:
  print('Eu não conheço a Maria!')

print(nomes.__contains__("Maria")) # outra forma de fazer o mesmo que o if


# Exemplo 3 de lista:
nomes = ["Wagner", "Antonio", "Jose", "Joao"] 

nomes[2:4] = "Maria" # Altera os elementos a partir do 3º até o 4º

# incluir elementos
nomes.append("Maria") # Adiciona um elemento no final da lista
nomes.insert(2, "Fernanda") # Adiciona um elemento na posição 2

# remover elementos
nomes.remove("Wagner") 

print(nomes)
removido = nomes.pop() # remove o último elemento da lista
removido = nomes.pop(2) # remove o elemento na posição 2 
print(nomes)
print(removido) # imprime o elemento removido

del nomes[1] # remove o elemento na posição 1
print(nomes)

# removendo a lista
"""
del nomes
print(nomes)
"""

nomes.clear() # limpa todos os elementos da lista
print(nomes)