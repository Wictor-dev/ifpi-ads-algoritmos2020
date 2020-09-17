def main():
    s = input('Digite a mensagem: ')
    n = len(s)
    if n%3 == 0:
        mensagem_original = 'SOS' * int(n/3)
        resultado = comparar_mensagens(s,n,mensagem_original)
        print(resultado)
    else:
        print('A mensagem tem formato inválido')
    
    


def comparar_mensagens(mensagem, tamanho, mensagem_original):
    count = 0
    for i in range(tamanho):
        if (mensagem[i] != mensagem_original[i]):
            count += 1
    
    return count


main()


