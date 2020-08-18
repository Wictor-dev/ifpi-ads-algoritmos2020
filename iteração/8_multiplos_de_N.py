def main():
    n = int(input('Digite o número: '))
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    while limite_inferior <= limite_superior:
        if(limite_inferior>1):
            if(verificar_multiplo(limite_inferior,n)):
                print(limite_inferior)
        limite_inferior += 1

def verificar_multiplo(numero, alvo):
    if numero % alvo == 0 or alvo%numero == 0:
        return True
    else:
        return False 

main()