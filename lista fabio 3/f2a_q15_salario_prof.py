def main():
    hora1 = int(input('Digite as horas trabalhadas pelo professor A: '))
    hora2 = int(input('Digite as horas trabalhadas pelo professor B: '))
    valor1 = int(input('Digite o valor por hora trabalhada do professor A: '))
    valor2 = int(input('Digite o valor por hora trabalhada do professor B: '))

    maior =  definir_maior_salario(hora1,valor1,hora2,valor2)

    print (maior)     


def definir_maior_salario(hora1,valor1,hora2,valor2):
    salario1 = hora1 * valor1
    salario2 = hora2 * valor2

    if salario1 > salario2:
        return f"A com R${salario1} de salário."
    elif salario1 == salario2:
        return f"Ambos os professores tem o mesmo salário (R${salario1})."
    else:
        return f"B com R${salario2} de salário."

main()

