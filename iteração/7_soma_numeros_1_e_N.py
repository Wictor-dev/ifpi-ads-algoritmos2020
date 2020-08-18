def main():
    n = int(input('Digite o número: '))

    result = 0
    count = 1
    while count <= n:
        result += count
        count += 1
    print(result)
    


main()