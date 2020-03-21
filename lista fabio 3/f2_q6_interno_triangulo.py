def main():
    n1 = int(input("Digite o primeiro ângulo: "))
    n2 = int(input("Digite o segundo ângulo: "))
    n3 = int(input("Digite o terceiro ângulo: "))

    triangulo = forma_triangulo(n1,n2,n3)

    print(f"A soma dos ângulos internos {n1},{n2},{n3} {triangulo}")

def forma_triangulo(n1,n2,n3):
    soma_interna = n1 + n2 + n3
    if soma_interna == 180:
        if n1 < 90 and n2<90 and n3<90:
            return "forma um triângulo acutângulo"
        elif n1 == 90 or n2 == 90 or n3 == 90:
            return "forma um triângulo retângulo"
        else:
            return "forma um triângulo obtusângulo"
    
    else:
        return "não forma um triângulo"


main()