def main():
    angle = int(input('Digite o ângulo: '))

    quadrante = definir_quadrante(angle)

    result = imprime_resultado(quadrante,angle)

    print (result)


def definir_quadrante(angle):
    if angle>= 0 and angle <= 360:
        if angle<=90:
            return f"O ângulo {angle} está no 1º quadrante"
        elif angle > 90 and angle <= 180:
            return f"O ângulo {angle} está no 2º quadrante"
        elif angle >180 and angle <= 270:
            return f"O ângulo {angle} está no 3º quadrante"
        else:
            return f"O ângulo {angle} está no 4º quadrante"
    else:
        return 0


def imprime_resultado(quadrante,angle):
    if quadrante == 0:
        return "angulo incompatível"
    else:
        return definir_quadrante(angle)


main()