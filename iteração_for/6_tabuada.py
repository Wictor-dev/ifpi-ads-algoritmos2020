def main():
    while True:
        n = int(input('Digite um número de 1 a 10: '))
        if(n >0):
            for i in range(11):
                print(f'{n} * {i} = {n * i}')
        else:
            print('é tudo 0 :)')
            break


main()
