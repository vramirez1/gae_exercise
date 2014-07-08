GAE Exercise
============

Pre-requisite
-------------

1. Download and install the [Google App Engine SDK for Python](https://developers.google.com/appengine/downloads)
1. Install a [git client](http://git-scm.com/downloads)
2. Login into [GitHub](https://github.com) or create an account
3. Set up GIT as explained in the [GitHub help](https://help.github.com/articles/set-up-git)
4. Go to [ThomasMarcel/gae_exercise](https://github.com/ThomasMarcel/gae_exercise) repository
5. Fork it
6. Add ThomasMarcel to the list of collaborators of your repository, on the repository page, in the menu on the right side of the screen: Settings > Collaborators
7. Clone your new repository `git clone https://github.com/username/repository_name.git`, the link appears on the right side under the "Settings" menu item  
_There are different files and folders inside the repository.  
The templates folder is holding all the templates that the webapp2 framework will be parsing.  
The static folder is for static files that will be accessed directly.  
The favicon.ico is the icon displayed by the navigator in the tab._  
8. Remove the lines regarding main.py and models.py from the .gitignore file

__You Will be using the [Google App Engine Python tutorial and documentation](https://developers.google.com/appengine/docs/python/gettingstartedpython27/introduction), as well as any other document you see fit to complete the exercise.__  

**Some tips**  
* At every step, remember to test it using the development server provided in the Google App Engine SDK, then push the changes to your repository. To do so, use the GUI to commit your changes, then push them. On a CLI, use `git add [file]...` to add files in the list to commit, so all the files you edited and created. then `git commit -m "commit message"` to commit the changes. Then git push , to push them to the repository on GitHub.
* If you encounter any issue or misbehavior during testing, check the dev appserver logs.
* Add logs at every step you deem useful. Unlike compiled languages, Python only has runtime errors. So writing in the log before the line that is causing an error might be a good way of investigating what went wrong.

*Feel free to contact me for help, revision or anything at thomas.alcala@gmail.com*

Exercise
--------
1. Create an app  
*Use the gae_exercise repository to create an app*  
	1. Create main.py with a WSGI handler or the root URL "/"  
*Tip: the handler in files look like `application = webapp2.WSGIApplication`*
	2. Modify the app.yaml configuration file to match your app settings
	3. Create a handler for the favicon.ico  
*Tip: check the static handlers declaration*
	4. Create a handler for the static folder
	5. Make the "/" handler in main.py print the classic "Hello World" sentence
	6. Try your application locally
2. Use templates
	1. Modify main.py to use the template templates/index.html instead of printing, and pass the "Hello World" string as a template value so it is displayed in the template  
*Tip: you can use webapp2, jinja or django*
	2. Modify the "/" handler to use templates/form.html template instead of templates/index.html
	3. Create a new handler that uses the templates/index.html template for the "/main" route, accepting POST method so the form in templates/form.html redirects to it
*Tip: the def get(self): line is to define a handling method for the GET HTTP method*
	4. Get the "username" variable from the form and pass it to the template so it is displayed
3. Use the datastore
	1. Define in a file called models.py a Datastore model for users called "User", with email, name and created to save the user creation date, which should be populated automatically when the entity is saved
	2. Define a method "get_by_email" of the class to get a user by his email address  
*Tip: use the @classmethod decorator*
	3. Modify the templates/form.html template to also ask for the user's email
	4. Modify the "/main" handler to check if there already is a user with the same email. I there isn't, then put it in the Datastore.
	5. Pass a template parameter to the templates/index.html template the user data, and modify the template to display his name and email
4. Optimize the use of the SDK
	1. Add parameters to the dev appserver at launch to use a specific datastore and blobstore  
*Tip: check the way to do it for your OS version of the SDK. This way you ensure consistency of your test data between tests*
5. Prepare your app for the next exercises
	1. Modify the current "/" handling to become "/register"  
_Modify app.yaml so the handler for "/", which uses main.py becomes instead "/register.*", and add a handler for "/main" which also uses main.py  
Modify the WSGIapplication in main.py to change "/" to "/register_
	2. Add a handler for "/.\*" that uses routes.py as script  
*routes.py imports the profile module, whose handler profile.handlers.ProfileHandler accepts an email parameter in its GET method, then looks or a  user registered in the datastore with the email  
You may have to use your /register route to register new users with email to your datastore if you didn't do so earlier during the exercises*
	4. Try to access your app adding as parameter the email of a user you previously set, e.g. [http://localhost:8080/?email=thomas.alcala@gmail.com](http://localhost:8080/?email=thomas.alcala@gmail.com)  
6. Use the blobstore  
_Take your time to check what routes.py does, what template it use_  
_**Check the different handlers in profile.handlers, what they do. For your conveniance a blobstore upload handler and a blob serve handler are already deined, very similar to the ones in the Google App Engine developers documentation, only to save the data in the datastore for persistence**_
	1. Add a blobkey property called "cv" to the User model to store the future key of the blob that will be used to store the CV of the user
	2. In a similar fashion as the user picture is working, modify the template to display a form to upload a CV when the user hasn't one
	3. Modify the upload handler and your form to be able to manage when the data sent by form is from the picture form or the cv form  
*Tip: you can add a hidden input in the form that goes by the name type and will have value "picture" in one form and "cv" in the other*
	4. When the user is redirected after saving the cv in the datastore, unlike with a picture that can be served directly, you should add a link to the file  
*Tip: Use something like `<a href="/serve/filekey">C.V.</a>`, passing the filekey to it by a template value*
7. Try the user service
8. Set cron jobs
9. Set asynchronous tasks
10. Set a channel
