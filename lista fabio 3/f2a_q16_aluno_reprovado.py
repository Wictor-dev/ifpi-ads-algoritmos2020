def main():
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))

    resultado = avaliar(nota1,nota2)

    print("O aluno está " + resultado)


def avaliar(nota1,nota2):
    if 0<= nota1 <= 10 and 0 <= nota2 <=10:
        media = (nota1 + nota2) / 2
        if media >= 7:
            return "aprovado"
        else:
            exame = float(input('Digite a nota do exame final: '))
            media_final = (exame + media) / 2
            if exame >= 0 and exame <= 10:
                if media_final>=5:
                    return "aprovado"
                else:
                    return "reprovado"
            else:
                return "em estado incompreensivel"
    else:
        return "em estado incompreensivel"


main()