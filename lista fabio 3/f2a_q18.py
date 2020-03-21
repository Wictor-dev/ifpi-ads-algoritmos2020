def main():
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite um número: '))
    print("Digite qual a operação matemática requisitada")
    operacao = int(input('(1 –Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão): '))

    resultado = calcular(num1,num2,operacao)

    print(resultado)


def calcular(n1,n2,op):
    if op >= 1 and op <=4:
        if op == 1:
            soma = n1 + n2
            return f"{n1} + {n2} = {soma}"
        elif op == 2:
            subtrair = n1 - n2
            return f"{n1} - {n2} = {subtrair}"
        elif op == 3:
            produto = n1 * n2
            return f"{n1} x {n2} = {produto}"
        else:
            quociente = n1 / n2
            result = " \n"
            result = result + f"{n1} \n"
            result =  result + f"____     =   {quociente} \n"
            result = result + f"{n2} \n"

            return result

main()
