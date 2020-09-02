def main():
    n = int(input('Digite a quantidade de frações: '))
    s = 0
    num = 1
    print('S = ', end='')
    for i in range(1,n+1):
        s += num/i
        if(i==n):
            print(f'{num}/{i} = ', end='')
        else:
            print(f'{num}/{i} +', end='')
        num += 2
    print(f'{s:.2f}')
main()