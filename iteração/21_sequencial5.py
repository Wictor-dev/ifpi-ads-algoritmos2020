def main():
    n = int(input('N: '))
    num = 1
    s = 0
    count = 1
    while num < n:
        s += count / num
        count += 2
        num += 1
        
    print(f'{count}/{num}')
    print(s)

main()
        
