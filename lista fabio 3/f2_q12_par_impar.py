def main():
    num = int(input("Digite o número: "))

    result = analisar_numero(num)
    
    print(f"O número {num} é {result}.")


def analisar_numero(num):
    if num % 2 == 0:
        return "par"
    elif num%2 != 0:
        return "ímpar"
    else:
        return "inválido"


main()