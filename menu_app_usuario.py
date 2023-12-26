#Debido a que sólo es un archivo que va a contener nuestras opciones
#Para simular el proceso de crud, no vamos a construir una clase.
from usuario_dao import UsuarioDAO
from logger_base import log
from usuario import Usuario

opcion = None
while opcion != 5:
    print("Opciones: ")
    print("1. Listar Usuarios")
    print("2. Agregar Usuario")
    print("3. Modificar Usuario")
    print("4. Eliminar Usuario")
    print("5. Salir")
    
    opcion = int(input("Escribe tu opción (1-5): "))
    
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios: 
            log.info(usuario)
    
    elif opcion == 2:
        username_var = input("Nombre de usuario a añadir: ")
        password_var = input("Cree una contraseña: ")
        usuario = Usuario(username=username_var, password= password_var)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f"Usuarios insertado: {usuarios_insertados}")
        
    elif opcion == 3:
        id_usuario_var= int(input("Escribe el id del usuario a modificar: "))
        username_var = input("Escriba el nuevo nombre de usuario: ")
        password_var = input("Escriba la nueva contraseña: ")
        usuario = Usuario (id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f"Usuarios actualizados: {usuarios_actualizados}")
    
    elif opcion == 4: 
        id_usuario_var = int(input("Escriba el id del usuario a eliminar: "))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f"Usuarios eliminados: {usuarios_eliminados}")
        
else: 
    log.info("Salimos de la aplicación...")