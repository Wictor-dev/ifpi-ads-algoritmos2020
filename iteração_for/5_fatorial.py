def main():
    numero = 1

    
    while numero > 0:
        result = 1
        numero = int(input("Digite o número: ") )
        for i in range(1,numero+1):
            
            result *= i
        print(f'O fatorial de {numero} é {result}')
        

main()