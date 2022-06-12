import time

def ser_poliedro(valor):
    valor = str(valor)
    if valor == valor[::-1]:
        return(True)
    else:
        return(False)

def poliedro():
    comecar_tempo = time.time()
    poliedro_lista = []
    debug_lista = []
    menor_valor = 900
    maior_valor = 999
    interacoes = 0

    for num1 in range(menor_valor, maior_valor):
        for num2 in range(menor_valor, maior_valor):
            interacoes += 1

            if ser_poliedro(num1*num2):
                poliedro_lista.append(num1*num2)
                debug_lista.append([num1,num2,num1*num2])
            if num1 == num2:
                break
    print('Imprimir poliedros:',poliedro_lista, num1, num2)
    print('debug_lista:', debug_lista)
    print('Interações:' , interacoes)
    print('Maior poliedro :', max(poliedro_lista))
    print('Tempo corrido:', time.time()-comecar_tempo)
    print('-----------Fim----------')

def poliedro_invertido():
    comecar_tempo = time.time()
    poliedro_lista = []
    debug_lista = []
    menor_valor = 100
    maior_valor = 999
    interacoes = 0
    menor_num2_valor = 100

    for num1 in range(maior_valor, menor_valor, -1):
        if num1 < menor_valor:
            break
        for num2 in range(maior_valor, menor_num2_valor, -1):
            interacoes += 1

            if ser_poliedro(num1*num2):
                poliedro_lista.append(num1*num2)
                menor_valor = max((num1*num2)/maior_valor,menor_valor)
                menor_num2_valor = num2
                debug_lista.append([num1,num2,(num1*num2)/maior_valor,menor_valor])
            if num1 == num2:
                break
    print('Imprimir poliedros:',poliedro_lista, num1, num2)
    print('debug_lista:', debug_lista)
    print('Interações:' , interacoes)
    print('Maior poliedro :', max(poliedro_lista))
    print('Tempo corrido:', time.time()-comecar_tempo)
    print('-----------Fim----------')

def poliedro_criar():
    nums=('9','8','7','6','5','4','3','2','1','0')
    interacoes = 0
    
    for dig1 in range(10):
        for dig2 in range(10):
            for dig3 in range(10):
                polie_str = nums[dig1] + nums[dig2] + nums[dig3] + nums[dig3] + nums[dig2] +nums[dig1]  
                poliedro = int(polie_str)
                
                menor_valor = int(poliedro/999)

                maior_valor = int(poliedro**0.5) + 1
                
                for digitos in range(menor_valor,maior_valor):
                    interacoes += 1
                    if poliedro % digitos == 0:
                       
                        return 'poliedro:', poliedro, 'digitos:',digitos, 'poliedro/digitos:', poliedro/digitos ,'interacoes:',interacoes

def poliedro_criar2():
    
    interacoes = 0
    
    for dig1 in range(9,0,-1):
        for dig2 in range(9,-1,-1):
            for dig3 in range(9,-1,-1):

                poliedro = dig1*100000 + dig2*10000 + dig3*1000 + dig3*100 + dig2*10 + dig1
                
                menor_valor = int(poliedro/999)
                maior_valor = int(poliedro**0.5)+1
                for digitos in range(menor_valor,maior_valor):
                    interacoes += 1
                    if poliedro % digitos == 0:
                        
                        return 'poliedro:',poliedro, 'digitos:',digitos, 'poliedro/digitos:', poliedro/digitos ,'interacoes:',interacoes

for func in ['poliedro_criar','poliedro_criar2']:
    corrido = 10 
    inicio = time.time()
    for run in range(corrido):
        retornar_valores = locals()[func]()
        fim = time.time()
    print(retornar_valores, 'Tempo total:', (fim-inicio)/corrido)

poliedro()
poliedro_invertido()
poliedro_criar()