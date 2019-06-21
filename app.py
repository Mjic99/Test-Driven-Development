class Mensaje:
    def __init__(self, contenido, remitente, destinatario):
        self.contenido = contenido
        self.remitente = remitente
        self.destinatario = destinatario

class Usuario:
    def __init__(self, nombre):
        self.id = id(self)
        self.nombre = nombre
        self.conversaciones = []

    def enviar_mensaje(self, destinatario, contenido):
        mensaje = Mensaje(contenido, self, destinatario)
        if self.conversacion_con(destinatario):
            self.conversacion_con(destinatario).mensajes.append(mensaje)
        else:
            conversa = Conversacion()
            conversa.usuarios.append(destinatario)
            conversa.usuarios.append(self.id)
            conversa.mensajes.append(mensaje)
            self.conversaciones.append(conversa)

    def conversacion_con(self, usuario):
        for conv in self.conversaciones:
            if all(user in [usuario.id, self.id] for ids in list(map(lambda usuario: usuario.id, conv))):
                return conv
        return False

    def get_contactos(self):
        contactos = []
        for conv in self.conversaciones:
            for usuario in conv.usuarios:
                if usuario.id != self.id:
                    contactos.append(usuario)

class Conversacion:
    def __init__(self):
        self.usuarios = []
        self.mensajes = []  