def main():
    n = int(input('Digite quantos elementos vc quer no vetor: '))
    vetor = []

    for i in range(n):
        vetor.append(input())
        
    if verificar_igualdade(vetor):
        print('Tem iguais')
    else:
        print('não tem iguais')


def verificar_igualdade(vetor):
    for i in range(len(vetor)):
        atual = vetor[i]
        for j in range(len(vetor)):
            if i == j:
                pass
            else:
                if atual == vetor[j]:
                    return True
    return False


main()