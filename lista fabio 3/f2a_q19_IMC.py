def main():
    h = float(input("Digite a altura em metros, ex(1.75 m): "))
    peso = float(input('Digite o peso em Kg, ex(65 kg): '))

    imc = peso / h ** 2

    resultado = analisar_corpo(h,peso,imc)

    print(resultado)


def analisar_corpo(h,peso,imc):
    if imc < 25:
        return "Você está com peso normal :), IMC = {:.2f}".format(imc)
    elif imc>= 25 and imc <=30:
        return "Você está acima do peso. IMC = {:.2f}".format(imc)
    else:
        return "Você está com obesidade mórbida :( {:.2f}".format(imc)


main()