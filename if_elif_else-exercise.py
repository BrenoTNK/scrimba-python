operador = input('Digite um operador (+, -, *, /) or "f" para converter Celcius em Fahrenheit: ')
num1 = float(input('Digite um número: '))

if operador.lower() == 'f':
    print(f'{num1} Celsius é igual a {(num1*9/5)+32} Fahrenheit')
else:
    num2 = float(input('Digite o segundo número: '))

    if operador == '+':
        print(f'O resultado é: {num1 + num2}')
    elif operador == '-':
        print(f'O resultado é: {num1 - num2}')
    elif operador == '*':
        print(f'O resultado é: {num1 * num2}')
    elif operador == '/':
        print(f'O resultado é: {num1 / num2}')
    else:
        print('Operador inválido!')