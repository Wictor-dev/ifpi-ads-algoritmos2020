def main():
    n = int(input('Digite a quantidade de números: '))

    media = 0
    count = 1
    while(count <= n):  
        print(f'N{count}:', end=' ') 
        valor = int(input())
        media += valor / n
        count += 1

    print(media)


main()
