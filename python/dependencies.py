from pycnic.core import WSGI, Handler
import futurice

class Dependencies(Handler):
    def get(self):
        req = self.request.args
        return futurice.get_similarities(req['variable'])

class app(WSGI):
    routes = [
        ('/dependencies', Dependencies()),
    ]
