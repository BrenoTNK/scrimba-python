def func(n):
    return lambda a: a*n

print(type(func(3)))

dobro = func(2)
print(dobro(3))
quadruplo = func(5)
print(quadruplo(3))

def cal_preco(inicial, cargaHoraria):
    return lambda horas : inicial + cargaHoraria * horas

corrida = cal_preco(10, 30)
corrida_premium = cal_preco(1, 25)
print(corrida(2))
print(corrida_premium(2))
print(cal_preco(1,25)(2))

print((lambda a,b,c : a+b+c)(2,3,4))
print((lambda a,b,c=2 : a+b+c)(2,3,4))
print((lambda a,b,c=2 : a+b+c)(2,c=3,b=4))
print((lambda *args : sum(args))(2,3,4,50))