def main():
    dia1 = int(input('Digite o Dia da primeira data: '))
    mes1 = int(input('Digite o mês da primeira data: '))
    ano1 = int(input('Digite o ano da primeira data: '))

    dia2 = int(input('Digite o Dia da segunda data: '))
    mes2 = int(input('Digite o mês da segunda data: '))
    ano2 = int(input('Digite o ano da segunda data: '))

    data_recente = definir_data_mais_recente(dia1,mes1,ano1,dia2,mes2,ano2)

    print(f"a data mais recente é {data_recente}")


def definir_data_mais_recente(dia1,mes1,ano1,dia2,mes2,ano2):
    if mes1==2 or mes2 == 2:
            if dia1>29 or dia2>29:
                return "data incompatível"
            else:
                if ano1 > ano2:
                    return f"{dia1}/{mes1}/{ano1}"
                elif mes1 == mes2:
                    if dia1 > dia2:
                        return f"{dia1}/{mes1}/{ano1}"
                    else:
                        return f"{dia2}/{mes2}/{ano2}"
                else:
                    return f"{dia2}/{mes2}/{ano2}"
    elif 30 >= dia1 >=1 and 12>=mes1>=1 and 2020>=ano1>=1:
        if 30 >= dia2 >=1 and 12>=mes2>=1 and 2020>=ano2>=1:
            if ano1 > ano2:
                return f"{dia1}/{mes1}/{ano1}"
            elif ano1 == ano2:
                if mes1>mes2:
                    return f"{dia1}/{mes1}/{ano1}"
                elif mes1 == mes2:
                    if dia1 > dia2:
                        return f"{dia1}/{mes1}/{ano1}"
                    else:
                        return f"{dia2}/{mes2}/{ano2}"
                else:
                    return f"{dia2}/{mes2}/{ano2}"
            else:
                return f"{dia2}/{mes2}/{ano2}"
        



main()
    