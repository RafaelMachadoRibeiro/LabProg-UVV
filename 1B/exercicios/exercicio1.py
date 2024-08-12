nomes = ['Jorge','Antonio', 'Fernanda', 'Jose', 'Joao', 'Wagner', 'Maria']

nomes_com_j = []


 # Gerar, a partir dessa lista de nomes, outra lista de nomes que tenham a letra 'J'.

for nome in nomes: # Para cada nome na lista de nomes
  if "J" in nome:
    nomes_com_j.append(nome)

print("NOMES COM J: ", nomes_com_j)

# USANDO LIST COMPREHENSION:
nomes_com_j = [nome for nome in nomes if nome.startswith('J')]
print("NOMES COM J: ", nomes_com_j)






# EXEMPLO 1
palavra = "Eu gosto de café"

if 'café' in palavra: # Verifica se a palavra 'café' está na string
  print('Tem café sim!')

# EXEMPLO 2
exemplo = "Maria"

if 'M' in palavra: # Verifica se a letra 'M' está na string
  print('Tem M')