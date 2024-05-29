import os
import msvcrt
import time
usuario = []
while True:
    print("""
    >>>Bienvenido usuario<<<
    OPCIONES:
    1) Iniciar Sesion
    2) Registrarse
    3) Eliminar usuario
    4) Salir """)
    print (usuario)
    
    opc = int(input('eliga una de las opciones:'))

    if opc == 1:
        pass
    elif opc == 2:
        correo = input('Ingrese correo: ')
        contraseña = input('Cree contraseña: ')

        perfil = {
            "correo": correo,
            "contraseña": contraseña
        }
        usuario.append(perfil)
        

    elif opc == 3:
        x = input('ingrese correo a eliminar')
        for x in(len(correo)):
            print(correo)
    else:
        break