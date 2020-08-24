def main():
    n = int(input('Digite a quantidade de funcionarios: '))

    inss = 8.5 / 100
    ir = 5 / 100

    count = 1
    while(count <= n):
        print(f'##### Funcionario {count} #####')
        cod_func = int(input('Digite o cod: '))
        num_horas_func = int(input('digite o num de horas: '))
        dependentes_func = int(input('digite o n de dependentes: '))
        
        num_horas = 12 * num_horas_func
        dependentes = 40 * dependentes_func
        salario = num_horas + dependentes


        salario_liquid = salario - ((inss * salario) + (ir * salario))

        print(f'O funcionario de codigo {cod_func} recebe R$ {salario} de salario bruto')
        print(f'é descontado R$ {inss * salario:.2f}  do inss e R${ir * salario:.2f}, o funcionario recebe {salario_liquid}')
        print('############################')

        count+=1
        

main()