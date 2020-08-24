def main():
    n = int(input('N: '))
    num = 1
    s = 0

    while num <= n:
        s += 1/num
        num += 1
    print(s)

main()
        
