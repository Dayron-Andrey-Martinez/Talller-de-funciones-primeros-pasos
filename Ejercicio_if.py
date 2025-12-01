#*********zona de funciones***********

def tomar_numero():
    numero_digitado= int(input("dijite un numero: "))
    return numero_digitado

def identificar_numero(numero):
    if numero > 0:
        return "El numero es positivo  "
    elif numero == 0:
        return " El numero es neutro: "
    else:
        return "El numero es negativo: "

def enviar_mensaje(numero_digitado, numero):
    mensaje= f"el numero {numero_digitado} es {numero}"
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#************codigo principal**********

dato_numero= tomar_numero()
tipo_numero= identificar_numero(dato_numero)
dato_mensaje=enviar_mensaje(dato_numero, tipo_numero)
imprimir_mensaje(dato_mensaje)
