# example.py
from pycnic.core import WSGI, Handler

class Hello(Handler):
    def get(self, variable="World"):
        print self.request.data
        return { "message":"Hello, %s!"%(variable) }

class app(WSGI):
    routes = [
        ('/', Hello()),
        ('/([\w]+)', Hello())
    ]
