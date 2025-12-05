# *************ZONA DE FUNCIONES *************
def capturar_datos():
    print("Digite la cantidad de números para sumar: ")
    cantidad = int(input())

    suma_parcial = 0  

    for i in range(cantidad):
        print("Digite el Número " + str(i+1) + ": ")
        numero = int(input())
        suma_parcial = suma_parcial + numero   

    return suma_parcial

def analizar_datos(suma_parcial):
    suma_total = suma_parcial
    return suma_total

def mostrar_resultados(total):
    print("La sumatoria total es: " + str(total))


# CODIGO PRINCIPAL
resultado_captura = capturar_datos()
resultado_analisis = analizar_datos(resultado_captura)
mostrar_resultados(resultado_analisis)
