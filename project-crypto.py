def enigma():
    chaves = 'abcdefghijklmnopqrstuvwxyz !'
    valores = chaves[-1] + chaves[0:-1]
    print(chaves)
    print(valores)

    dicio_e = dict(zip(chaves,valores))
    dicio_d = dict(zip(valores,chaves))

    dicio_e = dict(zip(chaves,valores))
    dicio_d = {value:key for key, value in dicio_e.items()}

    msg = input('Digite a mensagem secreta: ')
    modo = input('Cryptografia: Esconder (e) ou desvendar (d): ')

    if modo.lower() == 'e':
        nova_msg = ''.join([dicio_e[letras] for letras in msg])
    elif modo.lower() == 'd':
        nova_msg = ''.join([dicio_d[letras] for letras in msg])
    
    return nova_msg

print(enigma())