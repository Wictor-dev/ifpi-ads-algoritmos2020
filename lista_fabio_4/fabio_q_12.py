def main():
    n = int(input())
    vetor = []
    lista = []
    for i in range(n):
	    for j in range(n):
		    lista.append(int(input()))
	    vetor.append(lista)
	    lista= []

    
    d_principal = encontrar_diagonal_principal(vetor)
    soma_principais = somar_valores_vetor(d_principal)
    d_secundaria = encontrar_diagonal_secundaria(vetor)
    soma_secundaria = somar_valores_vetor(d_secundaria)
    print(f'Na matriz quadrada {n}x{n}')
    print_estilizado(vetor)
    print(f'Os valores da diagonal principal são: {d_principal}')
    print(f'A soma dos valores da diagonal principal é: {soma_principais}')
    print(f'Os valores da diagonal secundaria são: {d_secundaria}')
    print(f'A soma dos valores da diagonal secundaria é: {soma_secundaria}')


def print_estilizado(vetor):
    for i in range(len(vetor)):
        for j in vetor[i]:
            print(j, end='|')
        print('')


def somar_valores_vetor(vetor):
    soma = 0
    for i in vetor:
        soma += i

    return soma

def encontrar_diagonal_principal(vetor):
    lista = []
    n = len(vetor)
    for z in range(n):
        for x in range(n):
            if z == x:
                lista.append(vetor[z][x])

    return lista


def encontrar_diagonal_secundaria(vetor):
    ultimo = vetor[0][len(vetor) -1]
    lista = []
    n = len(vetor)
    c = 0
    for i in range(len(vetor)-1,-1,-1):
	    lista.append(vetor[i][c])
	    c += 1
        
    return lista

main()