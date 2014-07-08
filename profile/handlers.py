import os
import webapp2
import jinja2
import logging
import urllib

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

from models import User

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/../'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class ProfileHandler(webapp2.RequestHandler):
	def get(self):
		template_values = {}
		email = self.request.get('email')
		user = User.get_by_email(email)
		if user is not None:
			template_values['user'] = user
			if user.picture is None:
				upload_url = blobstore.create_upload_url('/upload')
				template_values['upload_url'] = upload_url
			else:
				blob_info = blobstore.BlobInfo.get(user.picture)
				try:
					blob_part = blobstore.fetch_data(blob_info, 0, 10)
				except Exception as e:
					try:
						logging.error('Couldn\'t fetch picture %s for user %s. Removing the picture for the user.' % (blob_info.filename, user.email))
						blob_info.delete()
					except AttributeError, e:
						logging.error('The picture for user %s couldn\'t be found. Removing it from the user properties.' % user.email)
					user.picture = None
					user.put()
					#template_values.pop('upload_url')

		logging.warning('os var: %s' % os.path.dirname(__file__))
                template = JINJA_ENVIRONMENT.get_template('templates/profile.html')
                self.response.write(template.render(template_values))

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):
		email = self.request.get('email')
		user = User.get_by_email(email)
		upload_files = self.get_uploads('picture')
		blob_info = upload_files[0]
		user.picture = blob_info.key()
		user.put()
		self.redirect('/?email=%s' % user.email)

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
	def get(self, resource):
		resource = str(urllib.unquote(resource))
		blob_info = blobstore.BlobInfo.get(resource)
		self.send_blob(blob_info)
