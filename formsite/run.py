from gevent.pywsgi import WSGIServer
import server

http_server = WSGIServer(('', 5000), server.app)
print("http://localhost:5000")
print("probably ok")
http_server.serve_forever()