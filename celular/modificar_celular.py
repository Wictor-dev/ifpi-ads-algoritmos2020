def modificar_celular(celulares,lista):
    menu = menu_modificar_celular()
    if len(lista) == 1:
        print('celular encontrado', lista)
        input('<enter> to continue... ')
        celular = lista[0] #nome do celular
        detalhes = detalhar_celular(celulares,celular)
        opcao = int(input(menu))
        operar_celular(celulares,celular, detalhes, opcao, menu) #lista de dicionarios/nome do celular/dicionario completo do celular/ opcao de modificação/ menu


    else:
        print('celulares encontrados', lista)
        print('Selecione o celular que você quer!')

        pos = int(input('Digite a posição do celular: '))
        celular = lista[pos - 1] # nome do celular
        detalhes = detalhar_celular(celulares, celular)
        print (f'O celular {celular} foi selecionado!')
        input('<enter> to continue...')
        opcao = int(input(menu))
        operar_celular(celulares,celular, detalhes, opcao, menu)



def operar_celular(celulares,nome, detalhes, opcao, menu):
    while opcao != 0:
        if opcao == 1:
            remover_celular(celulares, detalhes)
            break
        elif opcao == 2:        
            print(detalhes)
        elif opcao == 3:
            a = editar_celular(celulares, detalhes)
            if a == 'n':
                break
        elif opcao == 4:
            celulares.append(detalhes)
            print('O celular foi duplicado!')
        
        input('<enter> to continue')
        opcao = int(input(menu))
        
def remover_celular(celulares, celular):
    for i in range(len(celulares)):
        if celulares[i]['nome'] == celular['nome']:
            celulares.remove(celulares[i])
            print('O celular foi excluído')
            break        


def editar_celular(celulares, celular):
    opcao = input('Digite o que você deseja alterar do celular: (nome/marca/valor/tela/cam_frontal) ')

    if opcao.upper() == 'NOME':
        nome = input('Digite o novo nome: ')
        mudar_valor(celulares, opcao, nome, celular)       
    
    elif opcao.upper =='VALOR':
        valor = float(input("Digite o novo valor: "))
        mudar_valor(celulares, opcao, valor, celular)
    elif opcao.upper == 'MARCA':
        marca = input('Digite a nova marca: ')
        mudar_valor(celulares, opcao, marca, celular)
    elif opcao.upper == 'TELA':
        tela = input('Digite a tela: ')
        mudar_valor(celulares, opcao, tela, celular)
    elif opcao.upper == 'CAM_FRONTAL':
        cam_frontal = input('Possui câmera frontal? (sim/não)')
        mudar_valor(celulares, opcao, cam_frontal, celular)

    continua = input('Deseja continuar? (s/n)')
    return continua


def mudar_valor(celulares,opcao, valor, celular):   
    for item in celulares:
        if item == celular:
            item[f'{opcao}'] = valor
            print(f'{opcao} alterado(a)')

def menu_modificar_celular():
    menu = 'O que você deseja fazer com o celular?\n'
    menu += '1 - remover \n'
    menu += '2 - exibir detalhes \n'
    menu += '3 - editar \n'
    menu += '4 - duplicar\n'
    menu += '0 - nada \n'
    menu += 'Opção >>> '

    return menu

def detalhar_celular(celulares, celular):
    detalhe = {}
    for item in celulares:
        if celular.upper() in item['nome'].upper():
            detalhe['nome'] = item['nome']  
            detalhe['marca'] = item['marca']  
            detalhe['tela'] = item['tela']  
            detalhe['valor'] = item['valor']
            detalhe['cam_frontal'] = item['cam_frontal']
    
    return detalhe

def buscar_celular(celulares,choice, nome):
    lista = []
    for celular in celulares:
        if nome.upper() in celular[f'{choice}'].upper():
            lista.append(celular['nome'])
    
    return lista
