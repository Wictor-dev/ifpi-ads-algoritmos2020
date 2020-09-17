def main():
    s = input('Write your string: ')
    quantia = contador_de_strings(s)

    print(quantia)

def contador_de_strings(string):
    tamanho = len(string)
    count = 1
    for i in range(tamanho):
        valor = ord(string[i])
        if (122 >= valor >= 97):
                count = count
        else:
            count += 1

    return count


main()