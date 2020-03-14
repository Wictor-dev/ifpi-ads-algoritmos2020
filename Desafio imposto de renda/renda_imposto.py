def main():
    renda = float(input("Digite a sua renda: "))

    resultado = imprime_resultado(renda)

    print(resultado)



def imprime_resultado(renda):
    #Rendas da tabela atual e corrigida
    taxa_atual = calcula_imposto_atual(renda)
    taxa_corrigida = calcula_imposto_corrigido(renda)

    #Valor do imposto (Atual e corrigido)
    imposto_atual = renda * (taxa_atual/100)
    imposto_corrigido = renda * (taxa_corrigida/100)

    #renda líquida atual e corrigida
    renda_liquida_atual = renda - (renda * (taxa_atual/100))
    renda_liquida_corrigida = renda - (renda * (taxa_corrigida/100))

    print ("### Cálculo de imposto baseado na tabela atual ###")
    print ("De acordo com a tabela atual, a faixa de insenção que você pagaria seria {:.2f} %. Você pagará R$ {:.2f} de imposto".format(taxa_atual,imposto_atual), end=" ")
    print ("tendo um renda líquida de R$ {:.2f}".format(renda_liquida_atual))
    print ("--------------------------------------------------------")
    print ("### Cálculo de imposto baseado na tabela corrigida ###")
    print ("De acordo com a tabela atual, a faixa de insenção que você pagaria seria {:.2f} %. Você pagará R$ {:.2f} de imposto".format(taxa_corrigida,imposto_corrigido), end=" ")
    print ("tendo um renda líquida de R$ {:.2f}".format(renda_liquida_corrigida))


def calcula_imposto_atual(renda):
    if renda >=1:
        if renda <= 1903.98:
            return 0
        elif renda >= 1903.99 and renda <= 2826.65:
            return 7.5
        elif renda >= 2826.66 and renda <= 3751.05:
            return 15
        elif renda>= 3751.06 and renda <= 4664.68:
            return 22.5
        else:
            return 27.5
    else:
        return "Renda incompátivel"


def calcula_imposto_corrigido(renda):
    if renda >=1:
        if renda <= 3881.65:
            return 0
        elif renda >= 3881.66 and renda <= 5714.11:
            return 7.5
        elif renda >= 5714.12 and renda <= 7654.67:
            return 15
        elif renda>= 7654.68 and renda <= 9564.42:
            return 22.5
        else:
            return 27.5
    else:
        return "Renda incompátivel"



main()