amigos = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

for num, amigos in enumerate(amigos, 51):
    print(num, amigos)

for amigos in enumerate(amigos, 51):
    print(amigos)

for amigos in enumerate(enumerate(amigos, 51)):
    print(amigos)

for num, letra in enumerate('Python', start = 5):
    print(num, letra)

print(type(enumerate(amigos)))
print(list(enumerate(amigos)))
