## Installing

In Ubuntu/Debian:

```
sudo apt-get install python3
mkdir xss
cd xss
python3 -m venv venv
venv/bin/pip3 install twisted
```

## Making Vulnerable Application

### Hello $username Application 

This application will return “Hello!” for each GET-request:

```
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource

class WebApp(Resource):
    isLeaf = True
    def render_GET(self, request):
        return b'Hello!'

factory = Site(WebApp())
reactor.listenTCP(8880, factory)
reactor.run()
```

Output:
```
$ curl "http://localhost:8880"
<html><body>Hello!</body></html>
```

