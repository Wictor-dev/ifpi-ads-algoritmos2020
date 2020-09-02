def main():
   
    while True:
        n = int(input('Digite a quantidade de números: '))

        maior = 0
        list = []
        for i in range(n):
            num = int(input('Digite o número: '))
            list.append(num)
            if num > maior:
                maior = num
            
        print(f'Dentre os números {sorted(list)}, o maior é {maior}.')

        continua = input('Deseja continuar? (s/n)')
        if continua in ['n','N']:
            print('Adeus...')
            break

main()