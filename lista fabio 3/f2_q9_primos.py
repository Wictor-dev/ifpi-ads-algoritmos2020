def main():
    num = int(input("Digite o número: "))

    result = verifica_numero_primo(num)

    print(result)


def verifica_numero_primo(num):
    if num>=0 and num<=100:
        if num % num == 0 and num % 1 == 0 and not num % 2 == 0:
            return "é primo"
        elif num == 2:
            return "é primo"
        else:
            return "Não é primo"
    else:
        return "Número incompatível"


main()



