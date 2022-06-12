amigos = ['Joaquim', 'Ana', 'Maria', 'Carlos', 'Gabriel']
num = [650, 890, 321, 546, 112, 421]

print(min(num))     # Menor número (se for uma string seria alfabeticamente);
print(max(num))     # Maior número (se for uma string seria alfabeticamente);
print(sum(num))     # Soma dos números;

    # Ordem que foi escrita;
print(amigos)

    # Ordem inversa que foi escrita;
amigos.reverse()
print(amigos)

    # Ordem alfabetica ou crescente;
amigos.sort()
print(amigos)

    # Ordem alfabetica invertida ou decrecente;
amigos.sort(reverse = True)
print(amigos)

    # Adiciona um novo valor a lista;
amigos.append('Felipe')
print(amigos)

    # Adiciona um novo valor a lista em um lugar especifico;
# Forma 1:
amigos.insert(2, 'Henrique')
print(amigos)

# Forma 2:
amigos[4] = 'Vitor'
print(amigos)

    # Junta duas listas;
amigos.extend(num)
print(amigos)

    # Remove um valor da lista;
# Forma 1:
amigos.remove('Vitor')
print(amigos)

# Forma 2 (Se não for especficado a posição, ele remove o último valor):
amigos.pop()
print(amigos)

# Forma 3:
del amigos[2]
print(amigos)

    # Limpa a lista;
amigos.clear()
print(amigos)