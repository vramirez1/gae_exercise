import webapp2

from main import IndexHandler, MainHandler
from profile.handlers import ProfileHandler, UploadHandler, ServeHandler

application = webapp2.WSGIApplication([
	('/', ProfileHandler),
	('/register', IndexHandler),
	('/main', MainHandler),
	('/upload', UploadHandler),
	('/serve/([^/]+)?', ServeHandler),
], debug=True)
