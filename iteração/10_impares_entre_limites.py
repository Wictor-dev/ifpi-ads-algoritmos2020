def main():
    limite_superior = int(input('Digite o limite superior: '))
    limite_inferior = int(input('Digite o limite inferior: '))

    inicio = limite_inferior 
    fim = limite_superior
    while inicio < fim:
        if (inicio % 2 != 0):
            print(inicio)
        inicio += 1

main()