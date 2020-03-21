def main():
    n1 = int(input("Digite o primeiro lado: "))
    n2 = int(input("Digite o segundo lado: "))
    n3 = int(input("Digite o terceiro lado: "))

    triangulo = calcular_forma_triangulo(n1,n2,n3)

    print (triangulo)

def calcular_forma_triangulo(n1,n2,n3):
    if n1 + n2 >= n3 and n1 + n3 >= n2 and n3 + n2 >= n1:
        if n1 == n2 == n3:
            return "é equilátero"
        elif n1 == n2 and not n1 == n3:
            return "é isósceles"
        elif n1 == n3 and not n1 == n2:
            return "é isósceles"
        elif n2 == n3 and not n2 == n1:
            return "é isósceles"
        else:
            return "é escaleno"
    

    else:
        return "Não forma triângulo"

main()