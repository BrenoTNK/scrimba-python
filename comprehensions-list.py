num = [1,2,3,4,5,6,7,8,9]

    # Codigo 1;
nova_lista = []
for i in num:
    nova_lista.append(i*i)
print(nova_lista)
    # Equivalente;
nova_lista = [i*i for i in num]
print(nova_lista)

nova_lista = [i for i in num if i % 2 == 0]
print(nova_lista)

nova_lista = filter(lambda i : i % 2 == 0, num)
print(list(nova_lista))

    # Codigo 2;
nova_lista = []
for letra in 'spam':
    for num in range(4):
        nova_lista.append((letra, num))
print(nova_lista)
    # Equivalente;
nova_lista = [(letra, num) for letra in 'spam' for num in range(4)]
print(nova_lista)