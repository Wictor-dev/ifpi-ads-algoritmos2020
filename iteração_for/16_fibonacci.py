def main():
    n = int(input('Digite a quantidade de termos da sequência de fibonacci: '))

    anterior = proximo = 0
    for i in range(n):
        print(proximo, end=' ')
        proximo += anterior
        anterior = proximo - anterior
        if(proximo == 0):
            proximo += 1

main()