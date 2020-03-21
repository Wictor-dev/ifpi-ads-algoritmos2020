def main():
    dia_atual = 14
    mes_atual = 3
    ano_atual = 2020

    dia_nsc = int(input("Digite o dia de seu nascimento: "))
    mes_nsc = int(input("Digite o mês de seu nascimento: "))
    ano_nsc = int(input("Digite o ano de seu nascimento: "))

    idade = calcula_idade(dia_atual,mes_atual,ano_atual,dia_nsc,mes_nsc,ano_nsc)

    print(f"O sujeito tem {idade} anos")


def calcula_idade(dia_atual,mes_atual,ano_atual,dia_nsc,mes_nsc,ano_nsc):
    if ano_atual > ano_nsc:
        if mes_atual > mes_nsc:
            if dia_atual > dia_nsc or dia_atual<dia_nsc:
                return (ano_atual - ano_nsc) - 1
        elif mes_nsc > mes_atual:
            if dia_atual < dia_nsc or dia_atual > dia_nsc:
                return (ano_atual - ano_nsc) - 1
        elif mes_atual == mes_nsc:
            if dia_atual == dia_nsc:
                return ano_atual - ano_nsc
            elif dia_atual > dia_nsc:
                return ano_atual - ano_nsc
            elif dia_atual < dia_nsc:
                return (ano_atual - ano_nsc) - 1

main()