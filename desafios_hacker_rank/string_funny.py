def main():
    n = int(input())
    for i in range(n):
        s = input()
        tamanho = len(s)
        r = reverter_string(s,tamanho)
        lista = []
        
        for i in range(tamanho-1):
            lista.append(ord(s[i+1]) - ord(s[i]))

        if lista == r:
            print('funny')
        else:
            print('not funny')


def reverter_string(s,tamanho):
    r = s[::-1]
    lista_r = []
    for j in range(tamanho-1):
        lista_r.append(ord(r[j]) - ord(r[j+1]))
    return lista_r

main()