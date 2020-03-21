def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    num4 = int(input("Digite o quarto número: "))
    num5 = int(input("Digite o quinto número: "))

    media = calcular_media(num1,num2,num3,num4,num5)

    maior = define_maior(num1,num2,num3,num4,num5,media)
    
    print (f"a media é {media}")
    print (f"Número(s) maiores que a média ({maior})")

def define_maior(num1,num2,num3,num4,num5,media):
    if num1 == num2 == num3 == num4 == num5:
        return num1
    elif num1 > media:
        return num1
    elif num2 > media:
        return num2
    
        
        
    


def calcular_media(num1,num2,num3,num4,num5):
    media = (num1 + num2 + num3 + num4 + num5 ) / 5   

    return media
main()


