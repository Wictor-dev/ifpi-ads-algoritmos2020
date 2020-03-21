def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    result = dividir(n1,n2)

    print(result)

def dividir(n1,n2):
    resto = n1 % n2
    soma = n1 + n2
    n1_2 = n1 ** 2
    n2_2 = n2 ** 2
    if resto == 1:
        somar = soma + resto
        return f"A soma dos dois números com o resto é {somar}."
    elif resto == 2:
        if n1 % 2 == 0 and n2 % 2 == 0:
            return "Os dois números são pares"
        elif n1 % 2 == 0 and not n2 % 2 == 0:
            return f'O número {n1} é par e {n2} é impar'
        elif n1 % 2 != 0 and n2 % 2 == 0:
            return f'O número {n1} é impar e {n2} é par'
        else:
            return "Os dois números são ímpares"
    elif resto == 3:
        multi = (soma) * n1
        return f" a soma dos números divididos pelo primeiro é {multi}"
    elif resto == 4:
        divisao = (soma) / n2
        return f"A soma dos números divididos pelo segundo número é {divisao}"
    else:
        return f"{n1} ^2 = {n1_2} e {n2} ^2 = {n2_2}"


main()