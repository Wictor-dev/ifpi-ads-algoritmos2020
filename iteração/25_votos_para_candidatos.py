def main():

    c1 = 0 # candidato 1
    c2 = 0 # candidato 2
    c3 = 0 # candidato 3

    nulo = 0
    branco = 0

    n = int(input('Digite o total de eleitores: '))
    count = 1

    while count <= n:
        voto = int(input('Digite seu voto: '))
        
        if(voto == 1):
            c1 += 1
        elif(voto ==2):
            c2 += 1
        elif(voto == 3):
            c3 += 1
        elif(voto == 9):
            nulo += 1
        elif(voto == 0):
            branco += 1
        else:
            print('Valor inválido')
        count += 1

    print(f'{c1} votos para o candidato 1')#A)
    print(f'{c2} votos para o candidato 2')#A)
    print(f'{c3} votos para o candidato 3')#A)
    print(f'{nulo} votos nulos')#B)
    print(f'{branco} votos brancos')#C)

    vencedor = definir_vencedor(c1,c2,c3,nulo,branco)
    print(vencedor)


def definir_vencedor(c1,c2,c3,nulo,branco):
    if (c3 < c1 > c2 ):
        return 'O vencedor da eleição foi o candidato 1'
    elif(c3 < c2 > c1):
        return 'O vencedor da eleição foi o candidato 2'
    elif(c2 < c3 > c1):
        return 'O vencedor da eleição foi o candidato 3'
    else:
        return 'Não houve vencedores' 


main()


  