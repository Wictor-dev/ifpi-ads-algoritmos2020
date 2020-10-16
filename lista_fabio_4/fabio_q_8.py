def main():
    n = int(input('Digite quantos valores terá o vetor: '))
    vetor = []

    for i in range(n):
        vetor.append(int(input()))
    
    maior = encontrar_maior(vetor)
    menor = encontrar_menor(vetor)

    print(f'Nos números da lista {vetor} ')
    print(f'O maior é {maior}')
    print(f'O menor é {menor}')


def encontrar_maior(vetor):
    maior = vetor[0]
    for i in vetor:
        if i > maior:
            maior = i
    
    return maior


def encontrar_menor(vetor):
    menor = vetor[0]
    for i in vetor:
        if i < menor:
            menor = i
    
    return menor


main()