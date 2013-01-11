import cgi

import os
#import datetime
from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db


OPENID = [
    [ "google.com/accounts/o8/id", "Google", "icon-google-plus-sign" ],
    [ "yahoo.com", "Yahoo!", "icon-yahoo-sign" ],
    [ "myspace.com", "MySpace", "icon-myspace-sign" ],
    [ "aol.com", "AOL", "icon-aol-sign" ],
    [ "myopenid.com", "MyOpenID", "icon-myopenid-sign" ],
    [ "facebook.com", "Facebook", "icon-facebook-sign" ],
    [ "twitter.com", "Twitter", "icon-twitter-sign" ],
    [ "linkedin.com", "LinedkIn", "icon-linkedin-sign" ]
]


class MainPage(webapp.RequestHandler):
    """docstring for MainPage"""

    def __init__(self):
        """docstring for __init__"""
        self.usuario = users.get_current_user()

    def get(self):
        """docstring for get"""
        if self.usuario:
            estado = """
            <a class="btn btn-danger dropdown-toggle" data-toggle="dropdown" href="#">
              <i class="icon-user"></i> %s
              <span class="caret"></span>
            </a>""" % self.usuario
            menudrop = """<ul class="dropdown-menu">
              <li><a href="#">Perfil en GDev</a></li>
              <li class="divider"></li>
              <li><a href="%s">Salir</a></li>
            </ul>
            """ % users.create_logout_url(self.request.uri)
        else:
            estado = """
            <a class="btn dropdown-toggle" data-toggle="dropdown" href="#">
              <i class="icon-user"></i> %s
              <span class="caret"></span>
            </a>""" % "Ingresar"
            menudrop = """<ul class="dropdown-menu">"""
            for lista in OPENID:
                menudrop += """
                            <li><a href="%s"><i class="%s" style="font-size: 24px;"></i>%s</a></li>
                           """ % (users.create_login_url(federated_identity=lista[0]),
                                  lista[2],
                                  lista[1])
            menudrop += """</ul>"""
        template_values = {
                            'usuario': self.usuario,
                            'estado': estado,
                            'menudrop': menudrop,
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
