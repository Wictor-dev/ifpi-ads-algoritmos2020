def main():
    a0 = int(input('Digite o termo inicial: '))
    r = int(input('Digite a razão: '))
    limite = int(input('Digite o limite: '))
    
    while a0 < limite:
        print(a0)
        a0 *= r


main()