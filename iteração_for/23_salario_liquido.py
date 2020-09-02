import time
def main():
    n = int(input('Digite o número de funcionários: '))
    
    
    for i in range(1,n+1):
        inss = 8.5 / 100
        ir = 5 / 100
        print(f'#### Funcionário {i} ####')

        cod = int(input('Digite o código do funcionário: '))
        horas = int(input("Digite o número de horas trabalhadas: "))
        dependentes = int(input('Digite o número de dependentes: '))

        salario_bruto = (12 * horas) + (40 * dependentes)
        salario_liquido = salario_bruto - ((inss * salario_bruto) + (ir * salario_bruto))
        print('Analisando...')
        time.sleep(1)
        print('Análise concluída')
        print(f'O funcionário de código {cod} ganha R$ {salario_bruto} de salário bruto.')
        print(f'Descontando R$ {inss * salario_bruto:.2f} do INSS e R$ {ir * salario_bruto:.2f} do IR.')
        print(f'O funcionário ganha {salario_liquido:.2f}')


main()