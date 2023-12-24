from logger_base import log
class Usuario: 
    def __init__(self, id_usuario=None, username=None, password=None) -> None:
        self._id_usuario = id_usuario
        self._username = username
        self._password = password
        
    def __str__(self) -> str:
        return f"Usuario: {self._id_usuario}, {self._username}, {self._password}"
    
    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario
        
    @property
    def username(self):
        return self._username
    
    @username.setter
    def usernamme(self, username):
        self._username = username
    
    @property
    def password (self):
        return self._password
    
    @password.setter
    def password (self, password):
        self._password = password
    