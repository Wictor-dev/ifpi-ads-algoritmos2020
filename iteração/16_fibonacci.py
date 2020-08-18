def main():
    n = int(input('Digite a quantia de termos de fibonacci: '))

    if(n >= 2):
        anterior = 0
        proximo = 0
        while proximo < n:
            print(proximo)
            proximo += anterior
            anterior = proximo - anterior
            
            if(proximo == 0):
                proximo += 1



    

main()