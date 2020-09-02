def main():
    n = int(input('Digite o número de habitantes: '))

    total_filhos = salario_total = salario_menor_que_mil = 0

    for i in range(n):
        salario = float(input(f'Digite o salário do {i + 1}º habitante: '))
        filhos = int(input(f'Digite o número de filhos do {i + 1}º habitante: '))

        total_filhos += filhos
        salario_total += salario
        if (salario < 1000):
            salario_menor_que_mil += 1

    media_salario = salario_total / n
    media_filhos = total_filhos / n
    porcentagem_salario_menor_que_mil = salario_menor_que_mil * 100 / n

    print(f'A média dos salários é R$ {media_salario:.2f}.')
    print(f'A média de filhos é {media_filhos}.')
    print(f'A taxa de funcionários que ganham menos que R$ 1000.00 é de {salario_menor_que_mil} para {n}.', end = " ")
    print(f'Ou seja, {porcentagem_salario_menor_que_mil:.2f}%')




main()