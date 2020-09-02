def main():
    n = int(input('Digite N: '))
    s = 0
    num = n
    for i in range(1,n+1):  
        s += i/num
        if(i==n):
            print(f'{i}/{num} = ', end='')
        else:
            print(f'{i}/{num} + ', end='')
        num-=1
    print(f'{s:.2f}')


main()