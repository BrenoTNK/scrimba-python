try:
    # Faça isso:
    num = int(input('Digite um número entre 1 e 30: '))
    num1 = 30/num
    if num > 30:
        raise ValueError(num)
except ZeroDivisionError as err:
    # Exceto: 0;
    print(err, 'Não se pode dividir por 0!!!')
except ValueError as err:
    # Exceto: Valor não for 'int';
    print(err, 'Valor inválido')
except:
    # Exceto: Valor inválido;
    print('Inválido!')
else:
    # Se não houve excessão:
    print('30 dividido por', num, 'é:', 30/num)
finally:
    # Finalize;
    print('**Obrigado por jogar!**')
