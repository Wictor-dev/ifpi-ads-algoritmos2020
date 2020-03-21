def main():
    opcao = int(input("Digite qual é a opçao (1,2,3): "))
    num1 = int(input("Digite a primeira opção: "))
    num2 = int(input("Digite a segunda opção: "))
    num3 = int(input("Digite a terceira opção: "))

    result = verifica_opcao(opcao,num1,num2,num3)

    print (result)


def verifica_opcao(opcao,num1,num2,num3):
    if opcao >=1 and opcao <=3:
        if opcao == 1:
            return num1
        elif opcao == 2:
            return num2
        else:
            return num3
    else:
        return "Os únicos valores possíveis são (1,2,3)"

main()