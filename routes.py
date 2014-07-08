import webapp2

from profile.handlers import ProfileHandler, UploadHandler, ServeHandler

application = webapp2.WSGIApplication([
	('/', ProfileHandler),
	('/upload', UploadHandler),
	('/serve/([^/]+)?', ServeHandler),
], debug=True)
