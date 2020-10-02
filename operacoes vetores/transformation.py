def transformar(lista):
    menu = ' 1 - Dobrar todos os valores'
    menu += '\n 2 - Dobrar valores múltiplos de N'
    menu += '\n Opção >>> '
    opcao = int(input(menu))

    if opcao == 1:
        dobrar_valores(lista)
    elif opcao == 2:
        n = int(input('Digite o múltiplo: '))
        dobrar_multiplos_de_n(lista, n)
    else:
        print('Valor inválido')
    
    input('<enter> to continue... ')


def dobrar_valores(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] * 2
    
    print(lista)

def dobrar_multiplos_de_n(lista, n):
    for i in range(len(lista)):
        if lista[i] % n == 0:
            lista[i] = lista[i] * 2
    
    print(lista)


    