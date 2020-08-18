def main():
    numero = int(input("Digite o número: ") )

    result = 1
    count = 1
    while count <= numero:
        result *= count
        count += 1
    print(f'O fatorial de {numero} é {result}')


main()