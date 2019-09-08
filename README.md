# Daily Bytes
An online diary app where you can write whatever you wish and everything gets saved on the cloud.

### Built with
* [Django](https://www.djangoproject.com/)
* [Bulma](https://bulma.io/)

### Plug-ins / Add-ons
* [CKEditor](https://ckeditor.com/)
* [python-decouple](https://pypi.org/project/python-decouple/)
* [social-auth-app-django](https://github.com/python-social-auth/social-app-django)
* [Font Awesome](https://fontawesome.com)

### Hosted on
* [Heroku](https://www.heroku.com/)

## Screenshots
### Sign in 
![](https://github.com/thecoducer/daily-bytes/blob/master/screenshots/Screenshot%20from%202019-09-08%2000-24-20.png)
### Home
![](https://github.com/thecoducer/daily-bytes/blob/master/screenshots/Screenshot%20from%202019-09-08%2000-37-24.png)
### Add entry
![](https://github.com/thecoducer/daily-bytes/blob/master/screenshots/Screenshot%20from%202019-09-08%2000-37-34.png)

## Getting Started
To get a local copy up and running follow these simple example steps.

### Installation
1. Clone the repo ```git clone https://github.com/thecoducer/daily-bytes.git```
2. ```cd daily-bytes```
3. Create a virtual environment in Python: ```virtualenv -p python3 env```
4. Activate env: ```source env/bin/activate```
5. Install the requirements: ```pip3 install -r requirements.txt```

### Set up the environment variables
Create a ```.env``` file at the root of the directory and paste the below snippet in it and add your own credentials wherever required.

```
SECRET_KEY = 3s@8*%rpq13e03-5-_(9ow^*9f&c5rar(5wr%vhs=_k16@(r3i

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = <get one from Google developers console>
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = <get one from Google developers console>

SOCIAL_AUTH_KEY = <get one from Google developers console>
SOCIAL_AUTH_SECRET = <get one from Google developers console>

EMAIL_HOST_USER = <your email id>
EMAIL_HOST_PASSWORD = <your regular/app-specific password>

DEBUG = True

TIME_ZONE = <your time zone>

ALLOWED_HOSTS = localhost, .herokuapp.com, https://dailybytes.herokuapp.com, https://dailybytes.herokuapp.com/, http://dailybytes.herokuapp.com, http://dailybytes.herokuapp.com/
```

### Running the app
- Create the database: ```python manage.py migrate```
- Create admin account: ```python manage.py creatsuperuser```
- Run the app: ```python manage.py runserver```

## Improvements
Check [this](https://github.com/thecoducer/daily-bytes/issues/1) list

## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**. Go ahead and fork the project.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Twitter: [@thecoducer](https://twitter.com/thecoducer)
Email: [mayukh5741@gmail.com](mailto:mayukh5741@gmail.com)
