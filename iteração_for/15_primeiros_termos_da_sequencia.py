def main():
    while True:
        n = int(input('Digite a quantidade de termos da sequencia: ')) 

        item = 1 
        razao = 2 
        print('(', end = '') #  apenas formatação de print
        for i in range(n):
            if (i < n - 1):
                print(f'{item}', end = ', ') #  apenas formatação de print
            else:
                print(f'{item})') #  apenas formatação de print
            
            item += razao
            razao += 1

        continua = input("Deseja continuar? (s/n) ")

        if (continua in ['n','N','não','Não','nao','Nao']):
            print('Adeus...')
            break


main()