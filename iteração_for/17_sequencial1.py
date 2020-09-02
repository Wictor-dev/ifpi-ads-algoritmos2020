def main():
    n = int(input('Digite o ultimo denominador da sequencia: '))
    s = 0

    for i in range(1,n+1):
        s += 1/i
        if(i==n):
            print(f'1/{i} = ', end='')
        else:
            print(f'1/{i} + ', end='')
    print(f'{s:.2f}')

main()