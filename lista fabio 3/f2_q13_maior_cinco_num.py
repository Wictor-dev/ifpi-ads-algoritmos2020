def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    num4 = int(input("Digite o quarto número: "))
    num5 = int(input("Digite o quinto número: "))

    maior = define_maior(num1,num2,num3,num4,num5)
    menor = define_menor(num1,num2,num3,num4,num5)
    
    print (f"O maior é {maior} e o menor é {menor}.")


def define_maior(n1,n2,n3,n4,n5):
    if n1 != n2 != n3 != n4 != n5:
        if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
            return n1
        elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
            return n2
        elif n3>n1 and n3>n2 and n3>n4 and n3>n5:
            return n3
        elif n4>n1 and n4>n2 and n4>n3 and n4>n5:
            return n4
        else:
            return n5
    else:
        return "Os números não podem ser iguais"


def define_menor(n1,n2,n3,n4,n5):
    if n1 != n2 != n3 != n4 != n5:
        if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
            return n1
        elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
            return n2
        elif n3<n1 and n3<n2 and n3<n4 and n3<n5:
            return n3
        elif n4<n1 and n4<n2 and n4<n3 and n4<n5:
            return n4
        else:
            return n5
    else:
        return "Os números não podem ser iguais"
main()


