def main():
    vetor = []

    for i in range(8):
        vetor.append(int(input()))
    
    decimal = transformar_pra_decimal(vetor)
    hexadecimal = transformar_para_hexadecimal(decimal)
    
    print(f'O número binário {vetor} pode ser transformado em: ')
    print(f'{decimal} na base decimal')
    print(f'{hexadecimal} na base hexadecimal')


def transformar_para_hexadecimal(decimal):
    resto = ''
    while decimal > 0:
        valor = int(decimal % 16)
        decimal = decimal // 16
        if valor > 9:
            if valor == 10:
                resto += 'A'
            elif valor == 11:
                resto += 'B'
            elif valor == 12:
                resto += 'C'
            elif valor == 13:
                resto += 'D'
            elif valor == 14:
                resto += 'E'
            elif valor == 15:
                resto += 'F'
        else:
            resto += f'{valor}'
    return resto[::-1]


def transformar_pra_decimal(vetor):
    exp = 128
    valor = 0
    for i in range(8):
	    valor += vetor[i] * exp
	    exp = exp/2

    return int(valor)


main()