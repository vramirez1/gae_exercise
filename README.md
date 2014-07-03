GAE Exercise
============

Pre-requisite
-------------

1. Install a [git client](http://git-scm.com/downloads)
2. Login into [GitHub](https://github.com) or create an account
3. Set up GIT as explained in the [GitHub help](https://help.github.com/articles/set-up-git)
4. Go to [ThomasMarcel/gae_exercise](https://github.com/ThomasMarcel/gae_exercise) repository
5. Fork it
6. Add ThomasMarcel to the list of collaborators of your repository, on the repository page, in the menu on the right side of the screen: Settings > Collaborators
7. Clone your new repository - git clone https://github.com/username/repository_name.git - , the link appears on the right side under the "Settings" menu item  
_There are different files and folders inside the repository.  
The templates folder is holding all the templates that the webapp2 framework will be parsing.  
The static folder is for static files that will be accessed directly.  
The favicon.ico is the icon displayed by the navigator in the tab._  
  
__You Will be using the [Google App Engine Python tutorial and documentation](https://developers.google.com/appengine/docs/python/gettingstartedpython27/introduction), as well as any other document you see fit to complete the exercise.__  
  
**Some tips**  
* At every step, remember to test it using the development server provided in the Google App Engine SDK, then push the changes to your repository. To do so, use the GUI to commit your changes, then push them. On a CLI, use git add [file]... to add files in the list to commit, so all the files you edited and created. then git commit -m "commit message" to commit the changes. Then git push , to push them to the repository on GitHub.
* If you encounter any issue or misbehavior during testing, check the dev appserver logs.
* Add logs at every step you deem useful. Unlike compiled languages, Python only has runtime errors. So putting wrinting in the log before the line that is causing an error might be a good way of investigating what went wrong.

Exercise
--------
1. Create an app  
*Use the gae_exercise repository to create an app*  
	1. Modify the app.yaml configuration file to match your app settings
	2. Create a handler for the favicon.ico  
*Tip: check the static handlers declaration*
	3. Create a handler for the static folder
	4. Create main.py with a WSGI handler or the root URL "/"  
*Tip: the handler in files look like application = webapp2.WSGIApplication*
	5. Make the handler print the classis "Hello World" sentence
	6. Try your application locally
2. Use templates
	1. Modify main.py to use the template templates/index.html instead of printing, and pass the "Hello World" string as a template value so it is displayed in the template  
*Tip: you can use webapp2, jinja or django*
	2. Modify the "/" handler to use templates/form.html template instead of templates/index.html
	3. Create a new handler for the "/main" route, accepting POST method so the form in templates/form.html redirects to it  
*Tip: the def get(self): line is to define a handling method for the GET HTTP method*
	4. Get the "username" variable from the form and pass it to the template so it is displayed
3. Use the datastore
	1. Define in a file called models.py a Datastore model for users with email, name and created to save the user creation date, which should be populated automatically when the entity is saved
	2. Define a method of the class to get a user by his email address  
*Tip: use the @classmethod decorator*
	3. Modify the "/main" handler to check if there already is a user with the same email. I there isn't, then put it in the Datastore. Else, just pass a template parameter to the template with his data, to display his name and email on a modified template
