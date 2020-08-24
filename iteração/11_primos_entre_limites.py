def main():
    limite_superior = int(input('Digite o limite superior: '))
    limite_inferior = int(input('Digite o limite inferior: '))

    inicio = limite_inferior + 1
    fim = limite_superior
    while inicio < fim:
        if(inicio == 2 or inicio == 3 or inicio == 5 or inicio == 7):
            print(inicio)
        else:
            if(inicio % 1 == 0 and inicio % inicio == 0 and inicio % 2 != 0 and inicio % 3 != 0):
                if(inicio % 5 != 0 and inicio % 7 != 0):
                    print(inicio)
            
        
        inicio += 1

main()
