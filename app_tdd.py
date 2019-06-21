class Mensaje:
    def __init__(self, contenido, remitente, destinatario):
        self.contenido = contenido
        self.remitente = remitente
        self.destinatario = destinatario

        self.remitente.mensajes.append(self)
        self.destinatario.mensajes.append(self)

        self.remitente.contactos.add(destinatario)
        self.destinatario.contactos.add(remitente)

class Usuario:
    def __init__(self, nombre):
        self.id = id(self)
        self.nombre = nombre
        self.mensajes = []
        self.contactos = set()

    def mensajes_enviados_a(self, usuario):
        return list(filter(lambda mensaje: mensaje.destinatario.id == usuario.id, self.mensajes))

    def mensajes_recibidos_de(self, usuario):
        return list(filter(lambda mensaje: mensaje.remitente.id == usuario.id, self.mensajes))

    def conversacion_con(self, usuario):
        return list(filter(lambda mensaje: mensaje.destinatario.id == usuario.id or mensaje.remitente.id == usuario.id, self.mensajes))