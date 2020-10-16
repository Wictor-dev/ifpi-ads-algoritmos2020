def main():
    n = int(input())
    vetor = []
    adicionar_valores_na_lista(n,vetor)

    maior = encontrar_maior_soma(n,vetor)
    menor = encontrar_menor_soma(n,vetor)
    print(f'Na matriz quadrada {n} x {n}')
    print_estilizado(vetor)
    print(f'A linha com a maior soma de valores é a {maior}.')
    print(f'A linha com a menor soma de valores é a {menor}')


def print_estilizado(vetor):
    for i in range(len(vetor)):
        for j in vetor[i]:
            print(j, end='|')
        print('')


def encontrar_menor_soma(n,vetor):
    menor = somar_valores(vetor[0])
    indice = 1
    for i in range(1,n):
        valor = somar_valores(vetor[i])
        if valor < menor:
            menor = valor
            indice = i + 1
    
    return indice

def encontrar_maior_soma(n,vetor):
    maior = 0
    indice = 0
    for i in range(n):
        valor = somar_valores(vetor[i])
        if valor > maior:
            indice = i + 1
            maior = valor
    return indice


def somar_valores(vetor):
    count = 0
    for i in vetor:
        count += i
    
    return count


def adicionar_valores_na_lista(n,vetor):
    lista = []
    for i in range(n):
	    for j in range(n):
		    lista.append(int(input()))
	    vetor.append(lista)
	    lista= []


main()