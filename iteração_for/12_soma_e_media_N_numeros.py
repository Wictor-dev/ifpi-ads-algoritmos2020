def main():
    while True:       
        n = int(input('Digite a quantidade de Números: '))

        result = []
        soma = media = 0

        for i in range(1,n+1):
            num = int(input(f'Digite o {i}º número: '))
            result.append(num)
            soma += num

        media = soma / n

        print(f'A soma dos números {result} é igual a {soma}')
        print(f'A média dos números é {media:.1f}')

        continua = input('Ainda quer continuar? (s/n)')
        if continua == 'n' or continua == 'N':
            print('Adeus...')
            break


main()