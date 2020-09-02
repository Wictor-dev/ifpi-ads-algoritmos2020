def main():
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    inicio = limite_inferior + 1
    fim = limite_superior
    for i in range(inicio,fim):
        if(i == 2 or i== 3 or i == 5 or i == 7):
            print(i)
        else:
            if(i % 1 == 0 and i % i == 0 and i % 2 != 0 and i % 3 != 0):
                if(i % 5 != 0 and i % 7 != 0):
                    print(i)


main()
