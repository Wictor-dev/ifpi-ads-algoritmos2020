def main():
    hora_start = int(input('Digite a hora do começo do jogo: '))
    min_start = int(input('Digite os minutos da hora do começo do jogo: '))
    hora_end = int(input('Digite a hora do fim do jogo: '))
    min_end = int(input('Digite os minutos da hora do fim do jogo: '))

    tempo = calcular_tempo(hora_start,min_start,hora_end,min_end)

    print(tempo)
    

def calcular_tempo(hora_start,min_start,hora_end,min_end):
    min_total = min_start + min_end 
    hora_total = hora_end - hora_start
    if hora_start < hora_end and min_start < 60 and min_end < 60:
        
        if 0<=min_total< 60:
                  
            if hora_total == 1:
                if min_total == 1:
                    return f"O jogo tem {hora_total} hora e {min_total} minuto de duração."   
                else:
                    return f"O jogo tem {hora_total} hora e {min_total} minutos de duração."  
            else:
                return f"O jogo tem {hora_total} horas e {min_total} minutos de duração."
        elif min_total <= 120:
            hora_adc = min_total // 60
            minutos = min_total % 60
            hora_total_adc = hora_total + hora_adc
            return f"O jogo tem {hora_total_adc} horas e {minutos} minutos de duração."
        else:
            return "tempo ilegal"


    elif hora_end <= hora_start:
        hora_total2 = (24 - hora_start) + hora_end
        if 0<=min_total< 60:
                  
            if hora_total == 1:
                if min_total == 1:
                    return f"O jogo tem {hora_total2} hora e {min_total} minuto de duração."   
                else:
                    return f"O jogo tem {hora_total2} hora e {min_total} minutos de duração."  
            else:
                return f"O jogo tem {hora_total2} horas e {min_total} minutos de duração."
        elif min_total <= 120:
            hora_adc = min_total // 60
            minutos = min_total % 60
            hora_total_adc = hora_total2 + hora_adc
            return f"O jogo tem {hora_total_adc} horas e {minutos} minutos de duração."
        else:
            return "tempo ilegal"
        
        
    else:
        return ("tempo ilegal")


main()
