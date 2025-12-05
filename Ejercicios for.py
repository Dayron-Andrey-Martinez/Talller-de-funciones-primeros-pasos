# ZONA DE FUNCIONES 
def capturar_datos():
    suma_parcial = 0

    for i in range(0, 10, 2):
        numero = int(input("Digite el Número " + str(i+1) + ": "))
        suma_parcial = suma_parcial + numero

    return suma_parcial

def analizar_datos(suma_parcial):
    suma_total = suma_parcial   
    return suma_total

def mostrar_resultados(suma_total):
    print("La sumatoria total es:", suma_total)


# CODIGO PRINCIPAL
resultado_captura = capturar_datos()
resultado_analisis = analizar_datos(resultado_captura)
mostrar_resultados(resultado_analisis)
