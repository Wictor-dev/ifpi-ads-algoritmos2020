def contagem_de_valores(lista):
    menu = "***Contagem de valores***"
    menu += "\n 1 - Pares"
    menu += "\n 2 - Ímpares"
    menu += "\n 3 - positivos"
    menu += "\n 4 - negativo"
    menu += "\n 5 - primos"
    menu += "\n 6 - zerados"
    menu += "\n opção >>> "
    
    n = int(input(menu))
    a = contar_positivos(lista)
    if 7 > n > 0:
        if n == 1:
            contar_pares(lista)
        elif n == 2:
            contar_impares(lista)
        elif n == 3:
            print(a)
        elif n == 4:
            print(len(lista) - a)
        elif n == 5:
            contar_primos(lista)
        elif n == 6:
            contar_positivos(lista)
        
        
    else:
        print('Valor inválido')
    
    input('<enter> to continue...')


def contar_primos(lista):
    primos = []
    count = 0
    for i in lista:
        if i == 2 or i == 3 or i ==5 or i  == 7:
            count += 1
            primos.append(i)
        elif i > 7:
            if i % 2 != 0:
                if i % 3 != 0:
                    if i % 5 != 0:
                        if i % 7 != 0:
                            count += 1
                            primos.append(i)

    print(f'A quantidade de números primos é: {count} ')
    print(f'são eles {primos}')

    
    
def contar_positivos(lista):
    count = 0
    for i in lista:
        if i == 0:
            count += 1
    print(count)


def contar_pares(lista):
    count = 0
    for i in lista:
        if i % 2 == 0:
            count += 1
    print(count)


def contar_impares(lista):
    count = 0
    for i in lista:
        if i % 2 != 0:
            count += 1
    print(count)


def contar_positivos(lista):
    count = 0
    for i in lista:
        if i > 0:
            count += 1

    return count

