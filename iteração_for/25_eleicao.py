def main():
    n = int(input('Digite o número de eleitores: '))
    print('Vote usando os digitos de 0 a 9!')
    c1 = c2 = c3 = nulo = branco = 0
    for i in range(n):
        voto = int(input('Digite o código de voto: '))
        if (voto == 1):
            c1 += 1
        elif (voto == 2):
            c2 += 1
        elif (voto == 3):
            c3 += 1
        elif (voto == 0):
            branco += 1
        elif (voto == 9):
            nulo += 1
        else:
            print('Esse código é inválido!!!')
            print('Opções válidas  = (0,1,2,3,9)')

    print('### Resultado das eleições ###')
    print(f'{c1} votos para o candidato 1!')
    print(f'{c2} votos para o candidato 2!')
    print(f'{c3} votos para o candidato 3!')
    print(f'{branco} votos brancos!')
    print(f'{nulo} votos nulos!')

    vencedor = definir_vencedor(c1,c2,c3)

    print(vencedor)


def definir_vencedor(c1,c2,c3):
    if (c1 > c2 and c1 > c3):
        return f'O vencedor foi o candidado 1.'
    elif (c2 > c1 and c2 > c3):
        return f'O vencedor foi o candidado 2.'
    elif(c3 > c1 and c3 > c2):
        return f'O vencedor foi o candidado 3.'
    else:
        return "Não houve vencedores"

            

main()


