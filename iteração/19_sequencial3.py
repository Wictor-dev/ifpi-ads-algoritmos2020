def main():
    n = int(input('N: '))
    num = 1
    s = 0

    while n>=1:
        if (num % 2 == 0):
            s -= n/num
            print(f'{n}/{num}')
        else:
            s += num/n
            print(f'{num}/{n}')
        num += 1
        n -= 1
    
    print(s)

main()
        
