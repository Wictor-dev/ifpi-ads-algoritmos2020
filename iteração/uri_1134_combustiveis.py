def main():
    alcool = 0
    gasolina = 0
    diesel = 0

    codigo = int(input('código: '))

    while codigo != 4:
        if (codigo == 1):
            alcool += 1
        elif (codigo == 2):
            gasolina += 1
        elif (codigo == 3):
            diesel += 1

        codigo = int(input('código: '))

    print('MUITO OBRIGADO')
    print(f'alcool:{alcool}')
    print(f'gasolina:{gasolina}')
    print(f'diesel:{diesel}')

main()