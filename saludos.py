# zona de funciones
def capturar_nombre():
    nombre_usuario= input("escriba el nombre del cliente: ")
    return nombre_usuario
def capturar_rol():
    rol_usuario= input("escribe su rol: ")
    return rol_usuario
def hacer_saludo(nombre_usuario, rol_usuario):
    mensaje= " hola " + nombre_usuario + " rol "+ rol_usuario
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
    
def hora_actual():
    print("dijite la hora actual: ")
    hora_actual = input()
    return int(hora_actual)

def hora_del_dia(hora):
    if 0 <= hora < 12:
        return "mañana"
    elif 12 <= hora < 18:
        return "tarde"
    elif 18 <= hora < 24:
        return "noche"
    else:
        return "Hora no válida"
    
def mensaje_hora(hora_actual,hora_del_dia):
    mensaje = "la hora es :" + str (hora_actual) + " de la "  + hora_del_dia
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)

#zona principal
dato_usuario=capturar_nombre()
dato_rol= capturar_rol()
dato_mensaje=hacer_saludo(dato_usuario, dato_rol)
imprimir_mensaje(dato_mensaje)

dato_hora = hora_actual()
dato_del_dia = hora_del_dia(dato_hora)
mesaje= mensaje_hora(dato_hora,dato_del_dia)
imprimir_mensaje(mesaje)