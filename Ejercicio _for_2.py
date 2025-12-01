# ************* FUNCION CAPTURAR DATOS *************
def capturar_datos():
    print("Digite la cantidad de numeros para sumar: ")
    cantidad = int(input())  

    numeros = []  

    for i in range(cantidad): 
        print("Digite el Numero " + str(i+1) + ": ")
        numero = int(input())
        numeros.append(numero)

    return numeros

def analizar_datos(lista):
    suma = 0
    for num in lista:   
        suma = suma + num
    return suma

def mostrar_resultados(total):
    print("La sumatoria total es: " + str(total))


# ************* CODIGO CENTRAL MAIN *************
lista_numeros = capturar_datos()          # Captura
resultado = analizar_datos(lista_numeros) # Analiza
mostrar_resultados(resultado)             # Muestra
