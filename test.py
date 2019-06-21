import unittest
from app_tdd import *

class TestUsuarios(unittest.TestCase):
    
    def test_crear_usuarios_unicos(self):
        usuarios = []
        for i in range(10):
            usuarios.append(Usuario("Juan"))
        ids = list(map(lambda usuario: usuario.id, usuarios))

        self.assertEqual(len(ids), len(set(ids)))

    def test_mensajes_enviados_a(self):
        usuario1 = Usuario("Juan")
        usuario2 = Usuario("Pedro")
        for i in range(20):
            Mensaje("test", usuario1, Usuario("destinatario anonimo"))
            Mensaje("para usuario2", usuario1, usuario2)

        self.assertEqual(len(usuario1.mensajes_enviados_a(usuario2)), 20)
        self.assertEqual(usuario1.mensajes_enviados_a(usuario2)[0].destinatario.nombre, "Pedro")

    def test_mensajes_recibidos_de(self):
        usuario1 = Usuario("Juan")
        usuario2 = Usuario("Pedro")
        for i in range(20):
            Mensaje("test", usuario1, Usuario("destinatario anonimo"))
            Mensaje("para usuario2", usuario1, usuario2)

        self.assertEqual(len(usuario2.mensajes_recibidos_de(usuario1)), 20)
        self.assertEqual(usuario2.mensajes_recibidos_de(usuario1)[0].remitente.nombre, "Juan")

    def test_get_contactos(self):
        usuario1 = Usuario("Juan")
        for i in range(1,11):
            Mensaje("Hola", usuario1, Usuario("destinatario " + str(i)))
            Mensaje("Hola", Usuario("remitente " + str(i)), usuario1)

        lista_nombres = list(map(lambda contacto: contacto.nombre, usuario1.contactos))
        for i in range(1,11):
            self.assertIn("destinatario " + str(i), lista_nombres)
            self.assertIn("remitente " + str(i), lista_nombres)

    def test_conversacion_con(self):
        usuario1 = Usuario("Juan")
        usuario2 = Usuario("Pedro")
        Mensaje("Hola", usuario1, usuario2)
        Mensaje("Que tal", usuario2, usuario1)
        Mensaje("Como estas", usuario1, usuario2)

        textos = list(map(lambda mensaje: mensaje.contenido, usuario1.conversacion_con(usuario2)))
        self.assertEqual(textos, ["Hola", "Que tal", "Como estas"])

class TestMensajes(unittest.TestCase):
    usuario1 = Usuario("Juan")
    usuario2 = Usuario("Pedro")

    def test_crear_mensaje(self):
        mensajes_antes = len(self.usuario1.mensajes)
        mensaje = Mensaje("contenido de prueba", self.usuario1, self.usuario2)

        self.assertEqual(len(self.usuario1.mensajes) - mensajes_antes, 1)


if __name__ == '__main__':
    unittest.main()