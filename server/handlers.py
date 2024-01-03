from http.server import SimpleHTTPRequestHandler
from urllib.parse import urlparse

__all__ = ['RequestHandler']

class RequestHandler(SimpleHTTPRequestHandler):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, directory="web", **kwargs)

  def do_GET(self):
    parsed_path = urlparse(self.path)
    if not parsed_path.path.startswith("/api"):
      return super().do_GET()
    
    # your code goes here...