def main():
    n = 1
    
    while n>0:
        n = int(input('Digite o número: '))
        result = 0
        impressao = ''
        for i in range(1,n+1):
            result += i
            if(i<n):
                impressao += f'{i} + '
            else:
                impressao += f'{i}'
            
        print(f'{impressao} = {result}')
    


main()