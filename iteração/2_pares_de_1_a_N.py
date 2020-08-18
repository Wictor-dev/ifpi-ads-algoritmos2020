def main():
    n = int(input("Digite o número: "))

    inicio = 1
    while (inicio <= n):
        if(inicio%2 == 0):
            print(inicio)
        inicio += 1

main()
