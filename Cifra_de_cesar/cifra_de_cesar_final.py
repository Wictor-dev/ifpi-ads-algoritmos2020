def main():
    while True:
        frase = input('Digite a frase: ')
        rot = int(input('Digite a quantidade de rotações: '))

        frase_modificada = rotate_word(frase, rot)

        print(frase_modificada)
        continua = input('Deseja continuar? ')
        if (continua in ['n','nao','não','Não','NAO','NÃO']):
            print('Adeus...')
            break


def rotate_word(frase, rot):
    tamanho = len(frase)
    nova_frase = ''
    for i in range(tamanho):
        valor_frase = ord(frase[i])
        if(valor_frase<64 or (valor_frase>90 and valor_frase<97) or valor_frase>122):
            nova_frase += chr(valor_frase)
        if(valor_frase == 32):
            nova_frase += " "
        if (valor_frase>= 97 and valor_frase <= 122):
            nova_frase += modificar_minuscula(valor_frase,rot)      

        elif(valor_frase>= 65 and valor_frase <= 90):
            nova_frase += modificar_maiuscula(valor_frase,rot)

    return nova_frase

def modificar_minuscula(valor_frase,rot):
    transicao = valor_frase + rot
    letra_minuscula = ''
    if(transicao < 97):
        letra_minuscula += chr(122 - (96 - transicao))
    elif(transicao < 122):
        if (valor_frase == 122):
            if(rot>=1):
                letra_minuscula += chr(96 + rot)
            else:
                letra_minuscula += chr(valor_frase)
        else:
            letra_minuscula += chr(transicao)
    elif(transicao==122):
        letra_minuscula += chr(122)   
    else:
        letra_minuscula += chr(96 + (transicao - 122))
    return letra_minuscula

def modificar_maiuscula(valor_frase,rot):
    transicao = valor_frase + rot
    letra_minuscula = ''
    if(transicao < 65):
        letra_minuscula += chr(90 - (64 - transicao))
    elif(transicao < 90):
        if (valor_frase == 90):
            if(rot>=1):
                letra_minuscula += chr(64 + rot)
            else:
                letra_minuscula += chr(valor_frase)
        else:
            letra_minuscula += chr(transicao)
    elif(transicao==90):
        letra_minuscula += chr(90)    
    else:
        letra_minuscula += chr(64 + (transicao - 90))
    return letra_minuscula


main()