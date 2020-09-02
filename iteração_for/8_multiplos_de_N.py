def main():
    n = int(input('Digite o número: '))
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    for i in range(limite_inferior,limite_superior+1):
        if(i > 1):
            if(verificar_multiplo(i,n)):
                print(i)


def verificar_multiplo(numero, alvo):
    if numero % alvo == 0 or alvo%numero == 0:
        return True
    else:
        return False 

main()