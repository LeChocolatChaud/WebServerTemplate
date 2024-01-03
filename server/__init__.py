from http.server import ThreadingHTTPServer
from threading import Thread
from .handlers import RequestHandler

__all__ = ['run', 'stop']

__httpd: ThreadingHTTPServer | None = None

def run(port):
  """Run the server on the given port."""
  global __httpd
  if __httpd is not None:
    __httpd.shutdown()
  server_address = ('', port)
  __httpd = ThreadingHTTPServer(server_address, RequestHandler)
  t = Thread(target=__httpd.serve_forever)
  t.daemon = True
  t.start()
  print(f"Server running on port {port}")

def stop():
  """Stop the server."""
  global __httpd
  if __httpd is not None:
    __httpd.shutdown()
    __httpd = None
  print("Server stopped")
