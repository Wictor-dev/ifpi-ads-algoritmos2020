def main():
    num = float(input('Digite o número a ser arredondado: '))

    new_num  = arredondar(num)

    print(new_num)


def arredondar(num):
    decimal = num % 1
    num = num - decimal
    if decimal >= 0.5:
        num = num + 1
        return num
    elif decimal < 0.5:
        return num


main()