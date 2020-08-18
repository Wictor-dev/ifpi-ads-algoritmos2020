def main():
    n = int(input('Digite a quantidade de termos da sequencia (1,3,6,10,15...): '))

    sequencia = 0
    razao = 1 # número a ser somado na sequencia
    final = 1

    while final <= n:
        sequencia += razao
        razao += 1
        final += 1
        print(sequencia)


main()


