import os
import json
from modificar_celular import *

def main():

    # inicializar (recuperar do banco de dados )
    celulares = inicializar('celulares.bd')

    menu = tela_principal()
    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            print('Novo celular')
            celular = novo_celular()
            celulares.append(celular)
            print('Celular cadastrado com sucesso!')

        elif opcao == 2:
            mostrar_celulares(celulares)

        elif opcao == 3:
            choice = input('Você quer pesquisar por o celular por nome ou marca? ')
            
            if choice.upper() == 'NOME':
                nome = input('Digite o nome: ')
                celular_encontrado= buscar_celular(celulares, choice.lower(), nome)              

                modificar_celular(celulares, celular_encontrado)

            elif choice.upper() == 'MARCA':
                marca = input('Digite a marca: ')
                celular_encontrado = buscar_celular(celulares, choice.lower(), marca)

                modificar_celular(celulares, celular_encontrado)
            else:
                print('Escolha inválida')

        input('<enter> to continue...')
        opcao = int(input(menu))

    #finalizar (salvar banco)
    finalizar('celulares.bd', celulares)
        

# Arquivo 
def inicializar(nome_arquivo):
    celulares_carregados = []
    
    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        dados = arquivo.readline()
        celulares_carregados = json.loads(dados) 

    return celulares_carregados


def finalizar(nome_arquivo, celulares):
    dados = json.dumps(celulares)

    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close()

def mostrar_celulares(celulares):
    qtd = len(celulares)
    print(f'Listando {qtd} celulares')

    for celular in celulares:
        print('Nome:', celular['nome'])                
        print('marca:', celular['marca'])                
        print('Valor:', celular['valor'])                
        print(12 * '---')   


def novo_celular():
    # Obter dados
    nome = input('Nome: ')
    marca = input('Marca: ')
    tela = input('Tela("): ')
    valor = float(input('Valor (R$): '))
    cam_frontal = input('Camera frontal (sim/nao)')

    # criar o celular
    celular = {}
    celular['nome'] = nome
    celular['marca'] = marca
    celular['tela'] = tela
    celular['valor'] = valor
    celular['cam_frontal'] = cam_frontal   

    return celular                 

def tela_principal():
    menu = '***** App Jobs Cell *****\n'
    menu += '1 - Novo celular\n'
    menu += '2 - Listar celulares\n'
    menu += '3 - Pesquisar celulares por nome ou marca\n'
    menu += '0 - Sair\n'
    menu += '\nOpcão >>>'

    return menu

# Rodar a App
main()