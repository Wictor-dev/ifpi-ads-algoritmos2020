def main():
    # se nao achar o arquivo
    # https://stackoverflow.com/questions/49143852/trouble-opening-files-in-python-with-vs-code
    # "python.terminal.executeInFileDir": true,

    menu = '##### WordPplay #####\n' \
        + '1 - Palavras com + de 20 letras\n' \
        + '2 - Palavras sem "e"\n' \
        + '3 - Palavras sem letras proibidas \n' \
        + '4 - Palavras só com letras da lista \n' \
        + '5 - Palavras que contenham todas as letras da lista \n' \
        + '6 - Palavras que estão em ordem alfabética \n' \
        + '0 - Sair\n' \
        + '\nDigite uma opção: '

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            palavras_com_mais_de_20_letras()
        elif opcao == 2:
            palavras_sem_letra_e()
            
        elif opcao == 3:
            palavras_sem_letras_proibidas()
        
        elif opcao == 4:
            palavras_apenas_com_letras_da_lista()
        
        elif opcao == 5:
            palavras_que_contem_letras_da_lista()
        
        elif opcao == 6:
            palavras_em_ordem_alfabetica()
            
        else:
            print('Opção Inválida!')

        input('continuar <enter> ...')
        opcao = int(input(menu))

    print('Fim wordplay....')


def palavras_em_ordem_alfabetica():
    arquivo = open('words.txt')
    total = count = 0
    for letra in arquivo:
        palavra = letra.strip()
        total += 1
        if is_abecedarian(palavra):
            count += 1
            print(palavra)
    
    perc = (count / total) * 100
    print(f'Total de Palavras: {total}')
    print(f'Palavras em ordem alfabética: {count}')
    print(f'Percentual {perc} %')
    arquivo.close()

def is_abecedarian(word):
    for i in range(len(word)):
        if i < len(word) -1:
            if ord(word[i]) > ord(word[i+1]):
                return False
    return True

def palavras_que_contem_letras_da_lista():
    arquivo = open('words.txt')
    letras = ''
    n = int(input('Digite quantas letras você quer: '))
    total = count = 0
    for i in range(n):
        letras += input()
        if i==n-1:
            for linha in arquivo:
                palavra = linha.strip()
                total += 1
                if uses_only(palavra,letras):
                    count += 1
                    print(palavra)
                
    perc = (count / total) * 100
    print(f'Total de Palavras: {total}')
    print(f'Palavras apenas com letras da lista: {count}')
    print(f'Percentual {perc} %')
    arquivo.close()

def palavras_apenas_com_letras_da_lista():
    arquivo = open('words.txt')
    letras = ''
    n = int(input('Digite quantas letras você quer: '))
    total = count = 0
    for i in range(n):
        letras += input()
        if i==n-1:
            for linha in arquivo:
                palavra = linha.strip()
                total += 1
                if uses_all(palavra,letras):
                    count += 1
                    print(palavra)
                
    perc = (count / total) * 100
    print(f'Total de Palavras: {total}')
    print(f'Palavras apenas com letras da lista: {count}')
    print(f'Percentual {perc} %')
    arquivo.close()


def uses_all(palavra,letras):
    for i in letras:
        if i not in palavra:
            return False
    return True

def uses_only(palavra, letras):
    for i in palavra:
        if ord(i) == 32:
            pass
        else:
            if i not in letras:
                return False
    return True


def palavras_sem_letras_proibidas():
    arquivo = open('words.txt')
    n = int(input('Digite a quantidade de letras proibidas: '))
    proibida = ''
    total = count = 0
    for i in range(n):
        proibida += input()
        if i == n-1:
            for linha in arquivo:
                palavra = linha.strip()
                total += 1
                if avoids(palavra, proibida):
                    count += 1
                    print(palavra)

    perc = (count / total) * 100
    print(f'Total de Palavras: {total}')
    print(f'Palavras sem letras proibidas: {count}')
    print(f'Percentual {perc} %')
    arquivo.close()


def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def palavras_com_mais_de_20_letras():
    print('>> Palavras com + de 20 letras \n')
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) > 20:
            print(palavra)

    arquivo.close()


def palavras_sem_letra_e():
    print('>> Palavras sem letra "e" \n')
    arquivo = open('words.txt')
    total = 0
    palavras_sem_e = 0

    for linha in arquivo:
        palavra = linha.strip()
        total += 1
        if has_no_e(palavra):
            palavras_sem_e += 1
            print(palavra)

    perc = (palavras_sem_e / total) * 100
    print(f'Total de Palavras: {total}')
    print(f'Palavras sem "e": {palavras_sem_e}')
    print(f'Percentual {perc} %')
    arquivo.close()


def has_no_e(palavra):
    # return 'e' not in palavra
    for letra in palavra:
        if letra == 'e':
            return False

    return True


main()
