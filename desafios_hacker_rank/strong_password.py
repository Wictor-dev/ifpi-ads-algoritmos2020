def main():
    n = int(input('Digite o tamanho da senha: '))
    senha = input('Digite a senha: ')

    result = calcular_validade_senha(n,senha)
    print(result)


def calcular_validade_senha(n,senha):
    count = 0

    numbers = "0123456789" 
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    if (n<6):
        return 6 - len(senha)
    elif len(senha) > n:
        return 'Senha incompatível com o tamanho...'
    else:
        if buscar_caractere(senha,n,numbers) != 1:
            count += 1
        if buscar_caractere(senha,n,lower_case) != 1:
            count += 1
        if buscar_caractere(senha,n,upper_case) != 1:
            count += 1
        if buscar_caractere(senha,n,special_characters) != 1:
            count += 1
    
        return count


def buscar_caractere(senha, tamanho, string):   
    for i in range(tamanho):
            for j in range(len(string)):
                if senha[i] == string[j]:
                    return 1


main()