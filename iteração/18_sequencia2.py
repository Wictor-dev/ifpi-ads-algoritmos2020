def main():
    n = int(input('N: '))
    num = 1
    s = 0

    while num <= n:
        s += num/n
        num += 1
        n -= 1
    print(s)

main()
        
