def definir_quadrado(n):
    quadrado = n - 1
    raiz = 0
    while quadrado > 1:
        raiz = int(quadrado ** (1/2))
        if(raiz ** 2 == quadrado):
            return quadrado
            break
        else:
            quadrado -= 1
def main():
    n = int(input('Digite o número: '))

    resultado = definir_quadrado(n)

    print(resultado)


main()


