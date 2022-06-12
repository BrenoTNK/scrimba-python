semana1 = [7, 3, 42, 19, 15, 35, 9]
semana2 = [12, 4, 26, 10, 7, 28]
saldo = []

novo_dia = input('Digite o quanto foi vendido no novo dia: ')

semana2.append(int(novo_dia))

# saldo.extend(semana1)
# saldo.extend(semana2)

saldo = semana1 + semana2

# saldo.sort()

pior_dia = min(saldo) * 1.5
melhor_dia = max(saldo) * 1.5

print(f'O pior dia arrecadou: R$ {pior_dia}')
print(f'O melhor dia arrecadou: R$ {melhor_dia}')
print(f'Combinados foram: R$ {pior_dia + melhor_dia}')