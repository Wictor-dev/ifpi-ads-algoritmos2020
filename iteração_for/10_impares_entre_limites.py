def main():
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    inicio = limite_inferior 
    fim = limite_superior

    for i in range(inicio, fim):
        if (i % 2 != 0):
            print(i)
        
    
main()