def main():
    hab = int(input('Digite o numero de habitantes: '))

    media = media_filhos = salario_ate_mil = 0
    count = 1
    while count <= hab:
        print(f'### funcionario {count} ###')
        salario = int(input('Digite o salário: '))
        filhos = int(input('Digite o numero de filhos: '))
        media += salario
        media_filhos += filhos
        if(salario <= 1000):
            salario_ate_mil += 1
        count += 1

    media = media / hab
    media_filhos = media_filhos / hab
    print(f'A média dos salários é: R$ {media:.2f} ') # A)
    print(f'A média de filhos é {media_filhos}') #B)
    salario_ate_mil = salario_ate_mil * 100 / hab
    print(f'{salario_ate_mil:.0f}% dos habitantes possuem salario de até 1000 reais') #C)

main()
