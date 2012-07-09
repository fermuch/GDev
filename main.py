import cgi

import os
#import datetime
from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db


#class Preceptor(db.Model):
#    nombre = db.StringProperty(required=True, multiline=False)
#    apellido = db.StringProperty(required=True, multiline=False)
#    dni = db.IntegerProperty()
#    email = db.EmailProperty(required=True)


#class Alumno(db.Model):
#    nombre = db.StringProperty(required=True, multiline=False)
#    apellido = db.StringProperty(required=True, multiline=False)
#    dni = db.IntegerProperty(required=True)
#    curso = db.IntegerProperty(required=True)
#    division = db.StringProperty(required=True)
#    asignatura = db.StringProperty(required=True, multiline=False)
#    examen = db.StringProperty(required=True,
#                                multiline=False,
#                                choices=set(["LIBRES",
#                                            "PREVIOS",
#                                            "EQUIVALENCIAS",
#                                            "COMPLEMENTARIOS",
#                                            "REGULARES"]))
#    fecha_insc = db.DateTimeProperty(auto_now_add=True)
#    inscripto_por = db.UserProperty(required=True)


class MainPage(webapp.RequestHandler):
    def get(self):
        if users.get_current_user():
            estado = "Salir"
            diracceso = users.create_logout_url(self.request.uri)
        else:
            estado = "Ingresar"
            diracceso = users.create_login_url(self.request.uri)
        template_values = {
                            'usuario': users.get_current_user(),
                            'estado': estado,
                            'diracceso': diracceso,
            }
        path = os.path.join(os.path.dirname(__file__), "main.html")
        self.response.out.write(template.render(path, template_values))


#class Preceptores(webapp.RequestHandler):
#    def get(self):
#        if users.get_current_user():
#            estado = "Salir"
#            diracceso = users.create_logout_url('/')
#            plantilla = "preceptores.html"
#        else:
#            estado = "Acceder"
#            diracceso = users.create_login_url('/')
#            plantilla = "error.html"
#        contenido = ""
#        valores_plantilla = {
#                            'usuario': users.get_current_user(),
#                            'estado': estado,
#                            'diracceso': diracceso,
#            }
#        valores_plantilla['contenido'] = contenido
#        path = os.path.join(os.path.dirname(__file__), plantilla)
#        self.response.out.write(template.render(path, valores_plantilla))


application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
