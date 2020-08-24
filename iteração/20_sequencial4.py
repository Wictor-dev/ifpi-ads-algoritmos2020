def main():
    n = int(input('N: '))
    num = 1
    s = 0

    while num <= n:
        if(num % 2 == 0):
            s += 1/num
            print(f'- 1/{num}', end=' ')
        else:
            s -= 1/num
            print(f'+ 1/{num}',end=' ')
        num += 1
    print('')
    print(f'S = {s}')

main()
        
