def main():
    n = int(input('N: '))

    print('### Boi 1 ###')
    n_iden = int(input('Digite o número de identificação'))
    nome = input('DIgite o nome do boi: ')
    peso = float(input('Digite o peso do boi: '))

    n_iden_menor = n_iden
    nome_menor = nome
    peso_menor = peso
    count = 2
    while (n - 1) > 0:
        print(f'### boi {count} ###')
        iden = int(input('Digite o numero de identificação: '))
        boi_name = input('Digite o nome do boi: ')
        boi_peso = float(input('Digite o peso do boi:(KG) '))

        if(boi_peso > peso):
            peso = boi_peso
            nome = boi_name
            n_iden = iden
        if(boi_peso < peso_menor):
            peso_menor = boi_peso
            nome_menor = boi_name
            n_iden_menor = iden
        count +=1
        n -= 1
    print(f'O boi mais gordo é o {nome} com {peso} quilos, Nº de identificação ({n_iden})')
    print(f'O boi mais magro é o {nome_menor} com {peso_menor} quilos, Nº de identificação ({n_iden_menor})')




main()


