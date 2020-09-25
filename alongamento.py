def main():
    n = int(input("Quantidade de números: "))
    vetor = [-1]*n
    tipo_num = [0] * 4 # = [par,impar,positivo,negativo]
    # Primeiro print
    result = transformar(vetor,tipo_num)
    print(f'Números {result[0]}')
    print(f'Pares: {result[1][0]}')
    print(f'ìmpares: {result[1][1]}')
    print(f'Positivos: {result[1][2]}')
    print(f'Negativos: {result[1][3]}')
    
    # primeira modificação
    result = 0
    result = modificar(vetor,tipo_num)
    print(f'Números {result[0]}')
    print(f'Pares: {result[1][0]}')
    print(f'ìmpares: {result[1][1]}')
    print(f'Positivos: {result[1][2]}')
    print(f'Negativos: {result[1][3]}')
    media = calcular_media(result[0])
    print(f'A média dos valores é: {media:.2f}')

def transformar(vetor,tipo_num):
    for i in range(len(vetor)):
        vetor[i] = int(input())
        if vetor[i] % 2 == 0:
            tipo_num[0] += 1
            if vetor[i] > 0:
                tipo_num[2] += 1
            else:
                tipo_num[3] += 1
        else:
            tipo_num[1] += 1
            if vetor[i] > 0:
                tipo_num[2] += 1
            else:
                tipo_num[3] += 1
    mega_vetor = [vetor,tipo_num]
    return mega_vetor
    


def calcular_media(vetor):
    media = 0
    for i in vetor:
        media += i
    media = media / len(vetor)
    return media


def modificar(vetor, tipo_num): 
    tipo_num = [0] * 4
    for i in range(len(vetor)):
        if vetor[i] > 0:
            vetor[i] = vetor[i] * 2
            tipo_num[2] += 1
            if vetor[i] % 2 == 0:
                tipo_num[0] += 1
            else:
                tipo_num[1] += 1
        else:
            vetor[i] = vetor[i] / 2
            tipo_num[3] += 1
            if vetor[i] %2 == 0:
                tipo_num[0] += 1
            else:
                tipo_num[1] += 1
    mega_vetor = [vetor,tipo_num]
    return mega_vetor
    


main()