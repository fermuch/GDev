import cgi

import os
#import datetime
from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db


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


application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
