from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource

class WebApp(Resource):
    isLeaf = True
    def render_GET(self, request):
        return b'<html><body>Hello ' + request.args[b'name'][0] + b'!</body></html>'

factory = Site(WebApp())
reactor.listenTCP(8880, factory)
reactor.run()
