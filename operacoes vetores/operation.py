from contagem import contagem_de_valores
from transformation import transformar
def main():
    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar Valor posição'
    menu += '\n 3 - Remover do Final'
    menu += '\n 4 - Remover do Início'
    menu += '\n 5 - Remover de Posição Específica'
    menu += '\n 6 - Inserir valores em posição específica '
    menu += '\n 7 - Contar a quantidade de um tipo específico de número'
    menu += '\n 8 - Média dos valores'
    menu += '\n 9 - Contar a ocorrência de um valor'
    menu += '\n 10 - Transformar'
    menu += '\n 11 - limpar lista'
    menu += '\n 0 - Sair '
    menu += '\n\n Opção >>> ' 
    lista = []

    while True:
        opcao = int(input(menu))
        if opcao == 0:
            break
        elif opcao == 1:
            inserir_valores(lista)
        elif opcao == 2:
            mostrar_posicao(lista)
        elif opcao == 3:
            excluir_ultimo_valor(lista)
        elif opcao == 4:
            excluir_primeiro_valor(lista)
        elif opcao == 5:
            excluir_valor_determinado(lista)
        elif opcao == 6:
            inserir_valores_em_posicoes(lista)
        elif opcao == 7:
            contagem_de_valores(lista)
        elif opcao == 8:
            calcular_media(lista)
        elif opcao == 9:
            contar_quantidade_de_um_numero(lista)
        elif opcao == 10:
            transformar(lista)
        elif opcao == 11:
            lista.clear()
        else:
            print('Valor inválido')



    

def contar_quantidade_de_um_numero(lista):
    count = 0
    print(lista)
    valor = int(input('Qual valor você quer contar? '))
    for i in lista:
        if valor == i:
            count += 1
    
    print(f'Quantidade de vezes que o valor {valor} aparece: {count}')

def calcular_media(lista):
    total = 0
    for i in lista:
        total += i
    
    media = total / len(lista)
    print(f'{media:.2f}')

def inserir_valores_em_posicoes(lista):
    qtd = int(input('Digite quantos valores quer adicionar: '))
    for i in range(qtd):
        valor = int(input('Digite o valor: '))
        pos = int(input('Digite a posição: '))
        lista.insert(pos,valor)
    print(lista)
    print("Os valores foram inseridos com sucesso!")
    input('<enter> to continue... ')


def excluir_valor_determinado(lista):
    if len(lista) > 0:
        print(lista)
        valor = int(input('Digite a posição valor que voce quer excluir: '))
        lista.remove(lista[valor])
        print('Valor excluído com sucesso!!!')
    else:
        print('Lista vazia!')
        
    print(lista)
    input('<enter> to continue... ')


def excluir_primeiro_valor(lista):
    if len(lista) > 0:
        print(lista)
        print('Excluindo primeiro valor...')
        lista.remove(lista[0])
        print('primeiro valor excluido com sucesso!')
    else:
        print('Lista vazia')
    
    print(lista)
    input('<enter> to continue')


def excluir_ultimo_valor(lista):
    if len(lista) > 0:
        print(lista)
        print('Excluindo ultimo valor...')
        lista.remove(lista[len(lista) - 1])
        print('Ultimo valor excluido com sucesso!')
    else:
        print('Lista vazia')
    
    print(lista)
    input('<enter> to continue')

def mostrar_posicao(lista):
    if len(lista) > 0:
        print(lista)
        pos = int(input('Qual a posição do número que voce quer? '))
        print(lista[pos])
    else:
        print('Lista ainda vazia')
    input('<enter> to continue... ')

def inserir_valores(lista):
    qtd = int(input('Quantos valores deseja adicionar?'))
    for i in range(qtd):
        valor = int(input("Digite o valor... "))
        lista.append(valor)
    
    print ("valores adicionados com sucesso!")
    input("<enter> to continue... ")
main()