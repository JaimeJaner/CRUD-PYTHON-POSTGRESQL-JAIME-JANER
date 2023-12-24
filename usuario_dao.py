from cursor_del_pool import CursorDelPool 
from logger_base import log
from usuario import Usuario

class UsuarioDAO:
    """DAO -Data Access Object para la tabla de Usuario.
       CRUD - CREATE- READ - UPDATE -  DELETE TABLA USUARIO. 
    """
    
    _SELECT = "SELECT * FROM usuario ORDER BY id_usuario"
    _INSERTAR = "INSERT INTO usuario (username, password) VALUES (%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET username = %s, password = %s, WHERE id_usuario =%s"
    _ELIMINAR = "DELETE FROM usuario WHERE id_usuario= %s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor: #Creamos el cursor con nuestra capa de pool.
            log.debug("Seleccionando usuarios: ")
            cursor.execute(cls._SELECT) #Ejecutamos la sentencia SQL con el cursor.
            registros = cursor.fetchall()#Recuperamos los datos obtenidos por el cursor y almacenamos en una variable.
            usuarios = [] #Creamos una lista de objetos.
            for registro in registros: #Iteramos los datos recuperados para crear los objetos apartir de sus valores.
                usuario = Usuario(registro[0], registro[1], registro[2]) #Creamos un objeto de Usuario a partir de los datos obtenidos en cada iteración.
                usuarios.append(usuarios)# Y los almacenamos en la lista.
        return usuarios #Retornamos la lista de usuarios recuperada. 

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f"Usuario a insertar: {usuario}")
            valores = (usuario.username, usuario.password) #Tupla de valores para reemplazar los valores posicionales. 
            cursor.execute (cls._INSERTAR, valores) #Sentencia + valores posicionales.
            return cursor.rowcount #Retonamos el número de registros afectados.
    
    @classmethod
    def actualizar (cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(F"Usuario a actualizar: {usuario}")
            valores = (usuario.username, usuario.password, usuario.id_usuario,) #Se accede a estas propiedades a través de los métodos get.
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar (cls, usuario): #cls para ejecutar las variables de clase (En este caso ssentencias) y recibimos el objeto asociado a los valores.
        with CursorDelPool() as cursor: 
            log.debug(f"Usuario a eliminar {usuario}")
            valores = (usuario.id_usuario,) #Debe ser una tupla de valores, por eso la coma al final -en caso de ser valor único.-
            cursor.execute(cls._ELIMINAR, valores) 
            return cursor.rowcount
        