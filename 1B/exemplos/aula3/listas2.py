nomes = ['Antonio', 'Fernanda', 'Jose', 'Joao', 'Wagner', 'Maria']

print('###ITERANDO COM FOR###') 
for nome in nomes: # nome é uma variável temporária
  print(nome)

print(list(range(6)))

print('###ITERANDO PELO INDICE###') #performance mediana#
for i in range(len(nomes)): # i é uma variável temporária
  print(nomes[i])

print('###ITERANDO COM WHILE###') #pior performance#
i = 0 # variável de controle
while i < len(nomes): # condição de parada
  print(nomes[i]) # bloco de repetição
  i += 1 # incremento da variável de controle

print('###USANDO LIST COMPREHENSION###') #melhor performance#
[print(nome) for nome in nomes] # lista de compreensão