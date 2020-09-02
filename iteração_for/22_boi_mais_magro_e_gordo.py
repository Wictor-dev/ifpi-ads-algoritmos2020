def main():
    n = int(input('Digite o número de fichas: '))

    print("#### boi 1 ####")
    num_identificacao = int(input('Digite o número de identificação: '))
    nome = input('Digite o nome do boi: ')
    peso = float(input('Digite o peso do boi: '))

    num_iden_maior = num_iden_menor = num_identificacao
    nome_maior = nome_menor = nome
    peso_maior = peso_menor = peso

    for i in range(2,n+1):
        print(f"### boi {i} ####")
        num_iden = int(input('Digite o número de identificação: '))
        nome_boi_in = input('Digite o nome do boi: ')
        peso_boi_in = float(input('Digite o peso do boi: '))

        if peso_boi_in > peso:
            num_iden_maior = num_iden
            nome_maior = nome_boi_in
            peso_maior = peso_boi_in

        if peso_boi_in < peso:
            num_iden_menor = num_iden
            nome_menor = nome_boi_in
            peso_menor = peso_boi_in

    print(f'O boi mais pesado é {nome_maior}, nº identificação {num_iden_maior} com {peso_maior} quilos.')
    print(f'o boi mais magro é {nome_menor}, nº identificação {num_iden_menor} com {peso_menor} quilos.')
            
        
main()