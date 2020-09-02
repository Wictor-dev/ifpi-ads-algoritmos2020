def main():
    while True:
        n = int(input('Digite o número: '))

        for i in range(n,0,-1):
            raiz = int(i ** 0.5)
            if(raiz ** 2 == i):
                print(i)
                break
        
        continua = input('Deseja continuar? (s/n) ')
        print('------------------------')   

        if continua == 'n' or continua == 'N':
            print('Adeus...')
            break

main()