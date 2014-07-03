GAE Exercise
============

Pre-requisite
-------------

1. Install a [git client](http://git-scm.com/downloads)
2. Login into [GitHub](https://github.com) or create an account
3. [Set up GIT](https://help.github.com/articles/set-up-git) as explained in the GitHub help
4. Go to [ThomasMarcel/gae_exercise](https://github.com/ThomasMarcel/gae_exercise) repository
5. Fork it
6. Add ThomasMarcel to the list of collaborators of your repository, on the repository page, in the menu on the right side of the screen: Settings > Collaborators
7. Clone your new repository - git clone https://github.com/username/repository_name.git - , the link appears on the right side under the "Settings" menu item  
_There are different files and folders inside the repository.  
The templates folder is holding all the templates that the webapp2 framework will be parsing.  
The static folder is for static files that will be accessed directly.  
The favicon.ico is the icon displayed by the navigator in the tab._

Exercise
--------
__At every step, remember to push the changes to your repository.  
To do so, use the GUI to commit your changes, then push them. On a CLI, use git add [file]... to add files in the list to commit, so all the files you edited and created. then git commit -m "commit message" to commit the changes. Then git push , to push them to the repository on GitHub.__

1. Create an app  
*Use the gae_exercise repository to create an app*  
	1. Modify the app.yaml configuration file to match your app settings
	2. Create a handler for the favicon.ico
	3. Create a handler for the static folder
	4. Create main.py with a handler or the root URL "/"
	5. Make the handler print the classis "Hello World" sentence
	6. Try your application locally
2. Use templates
	1. Modify main.py to use the template templates/index.html instead of printing, and pass the "Hello World" string as a template value so it is displayed in the template
