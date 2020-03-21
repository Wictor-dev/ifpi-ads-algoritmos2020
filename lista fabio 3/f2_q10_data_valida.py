def main():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    result = verifica_data(dia,mes,ano)

    print(result)


def verifica_data(dia,mes,ano):
    if ano >= 1:
        if mes >=1 and mes <=12:
            if mes == 2:
                if 1 <= dia <= 28:
                    return f"A data {dia}/{mes}/{ano} é válida"
                else:
                    return f"A data {dia}/{mes}/{ano} não é válida"
            elif dia >=1 and dia <= 30:
                return f"A data {dia}/{mes}/{ano} é válida"
            else:
                return f"A data {dia}/{mes}/{ano} não é válida"
        else:
            return f"A data {dia}/{mes}/{ano} não é válida"
    else:
        return f"A data {dia}/{mes}/{ano} não é válida"


main()