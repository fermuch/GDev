class UsuarioG(db.Model):
    def __init__(self):
        if users.get_current_user():
            estado = "Salir"
            diracceso = users.create_logout_url(self.request.uri)
        else:
            estado = "Acceder"
            diracceso = users.create_login_url(self.request.uri)
    nombre = db.StringProperty(required=True, multiline=False)
    apellido = db.StringProperty(required=True, multiline=False)
    email = db.EmailProperty(required=True)
    programacion = db.StringProperty(required=True,
                                multiline=False,
                                choices=set(["Java",
                                            "Python",
                                            "PHP",
                                            "Ruby",
                                            "Rails",
                                            "Otros"]))

"""1. Habilidades Tecnicas.
Programación.
Java.
Python.
PHP.
otros
Analisis y Diseño.
Diseño Grafico.
Diseño GUI.
Testing
Administración de Proyectos.
2. Tiempo.
- Fijo para el proyecto en particular.
- Tiempo libre general para proyectos.
3. GTUG al que pertenece.
4. Proyectos en los que participa.
- Nombres y tiempo que les dedica por semana.
5. Habilidades No Tan Técnicas. (creatividad, capacidad para organizar, documentador, traductor, negociación, solución de conflictos, educción ...)
6. Información de Contacto. (Mail, Móvil, link a: Twitter, G+, LinkedIn, Facebook)
7. Repositorios que Utiliza. (Git, SVN, BZR, etc.)
8. Metodologías Agiles."""
