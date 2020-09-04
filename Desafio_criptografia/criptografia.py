def main(): 
    n = int(input('Digite quantas frases você quer criptografar: '))
    for i in range(n):
        texto = input('Digite a frase a ser criptografada: ')
        novo_texto = ''
        cripto = criptografar_frase(texto,novo_texto)
        print(cripto)

def criptografar_frase(texto,novo_texto):
    tamanho_string = len(texto)

    for i in range(3):
        if(i == 0):
            for x in range(tamanho_string):
                valor_texto = ord(texto[x])
                if(valor_texto >= 65 and valor_texto <= 90) or (valor_texto >= 97 and valor_texto <= 122):
                    novo_texto += chr(valor_texto + 3)
                else:
                    novo_texto += texto[x]
        elif(i==1):
            # novo_texto = novo_texto[::-1]
            novo_texto = inverter_string(novo_texto, tamanho_string)
        else:
            metade_tamanho = tamanho_string // 2
            texto_deslocado_esquerda = deslocar_palavra_para_esquerda(novo_texto, tamanho_string)
            for z in range(metade_tamanho, tamanho_string):
                novo_texto = novo_texto[:-1]
                if (z == tamanho_string - 1):
                    for y in range(metade_tamanho, tamanho_string):
                        novo_texto += texto_deslocado_esquerda[y]
    
    return novo_texto

def inverter_string(string, tamanho_string):
    string_invertida = ''
    for i in range(tamanho_string -1, -1, -1):
        string_invertida += string[i]
    return string_invertida

def deslocar_palavra_para_esquerda(novo_texto,tamanho_string):
    text =''
    for i in range(tamanho_string):
        valor_texto = ord(novo_texto[i])
        text += chr(valor_texto - 1)
    return text       

main()