
def capturar_datos():
    print("Digite un numero del 1 al 12")
    numero = int(input())
    return numero


def analizar_datos(num):
    match num:
        case 1:
            return "Enero"
        case 2:
            return "Febrero"
        case 3:
            return "Marzo"
        case 4:
            return "Abril"
        case 5:
            return "Mayo"
        case 6:
            return "Junio"
        case 7:
            return "Julio"
        case 8:
            return "Agosto"
        case 9:
            return "Septiembre"
        case 10:
            return "Octubre"
        case 11:
            return "Noviembre"
        case 12:
            return "Diciembre"
        case _:
            return "Número inválido"



def mostrar_resultados(mes):
    print("El mes correspondiente es:", mes)



numero = capturar_datos()          
mes = analizar_datos(numero)       
mostrar_resultados(mes)            
