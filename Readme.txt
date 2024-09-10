The projects starts with a syntex #django-admin start project facebook 
The project name is facebook
After creating the project you will have a lot of files that are made by django 
like __init.py , asgi.py , setting.py, urls.py ,wsgi.py files like these will be help full in making a compelete website 
for running the project commands are as follows #python manage.py runserver
The project will be run on the local host and port 8000
After deploying the app will create app for the project apps are the modules and the interface of the user interaction 
The django works on the principle of MVT
MVT stands for Model View Template
The Model is the database of the project
The View is the interface of the user interaction
The Template is the html file of the project
Now we create an app by using command # python manage.py start app snapchat
The app name is snapchat
The app will be created in the project directory
The app will have the following files
__init.py,admin.py ,apps.py,test.py,views.py, 
we will create some additional files such as models.py for the database, urls.py for setting the connection between the project and the app , views.py for the function for the apps icons 
The app will be registered in the project by using the following command
#python manage.py makemigrations snapchat
#python manage.py migrate snapchat
The app will be registered in the project and the database will be created for the app
we also have to create a static and template(html ) for the frontend user intraction 
The static files are the files that are used for the frontend user interaction such as css, js,
The template files are the html files that are used for the frontend user interaction
These templates will be connected to eachother from %extend%base.html 
The base.html is the main html file that is used for the frontend user interaction
The base.html will be extended by all the other html files in the project

