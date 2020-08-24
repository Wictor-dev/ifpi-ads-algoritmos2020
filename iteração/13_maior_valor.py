def main():
    n = int(input('Digite o valor de N: '))

    maior_valor = 0
    count = 1

    while count <= n:
        valor = int(input())

        if(valor > maior_valor):
            maior_valor = valor

        count += 1

    print('O maior valor é',maior_valor)


main()
