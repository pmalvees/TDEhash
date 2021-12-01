# em python o dict é uma implementação de uma hashtable
hashtable = {}

# Inserindo chaves/valores
hashtable['Amendoim'] = 10
hashtable['Nozes'] = 15
hashtable['Uva'] = 20

# Inserindo com chave já existente
hashtable['Uva'] = 44

# Imprimindo as chaves
for key in hashtable.keys():
  print(f'Chave: {key}')

# Imprimindo valores
for val in hashtable.values():
  print(f'Valor: {val}')

# Imprimindo os pares chave/valor
for k, v in hashtable.items():
  print(f'Chave: {k} - Valor: {v}')

# Imprimindo chave inexistente
# Maneira incorreta pois quebra
# print(hashtable['nao-existe'])

# Maneira correta, valor padrão caso nao exista
print(hashtable.get('nao-existe'))