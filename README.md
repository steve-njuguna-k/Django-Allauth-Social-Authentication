# Django-Allauth-Social-Authentication
This is a Django Social Login &amp; Sign Up App using sites like GitHub, Google, Twitter &amp; LinkedIn to access a website. This is all achieved using Django Allauth 

![](https://github.com/steve-njuguna-k/Django-Allauth-Social-Authentication/blob/master/src/static/img/Screenshot-1.PNG)

![](https://github.com/steve-njuguna-k/Django-Allauth-Social-Authentication/blob/master/src/static/img/Screenshot-2.PNG)

# Functionalities
- You Can Log In With Google

![](https://github.com/steve-njuguna-k/Django-Allauth-Social-Authentication/blob/master/src/static/img/Screenshot-3.PNG)

- You Can Log In With LinkedIn

![](https://github.com/steve-njuguna-k/Django-Allauth-Social-Authentication/blob/master/src/static/img/Screenshot-4.PNG)

- You Can Log In With GitHub

![](https://github.com/steve-njuguna-k/Django-Allauth-Social-Authentication/blob/master/src/static/img/Screenshot-5.PNG)

- You Can Log In With Twitter

![](https://github.com/steve-njuguna-k/Django-Allauth-Social-Authentication/blob/master/src/static/img/Screenshot-6.PNG)

# Project Setup Instructions
1) Git clone the repository 
```
https://github.com/steve-njuguna-k/Django-Allauth-Social-Authentication.git
```
2. Go To Project Directory
```
cd Django-Allauth-Social-Authentication
```
3. Create Virtual Environment
```
virtualenv env
```
4. Active Virtual Environment
```
env\scripts\activate
```
5. Install Requirements File
```
pip install -r requirements.txt
```
6. Migrate Database
```
py manage.py migrate
```
7. Create Super User
```
py manage.py createsuperuser
```
8. Log into Django Admin
```
http://127.0.0.1:8000/admin
```
9. Head over to Social Applications and fill in the following details:
```
Provider: (Google, Twitter, LinkedIn, GitHub)
Name: (Google, Twitter, LinkedIn, GitHub) OAuth App
Client id: <The client ID you created in your developer account>
Secret key: <The Secret key you created in your developer account>
Sites: 127.0.0.1:8000

NB: For Twitter, the client ID is the API Key. The rest use the client IDs provided
```
10. Logout of Django Admin & Run the Project
```
py manage.py runserver
```
11. Head over to URL
```
http://127.0.0.1:8000/login
```

© 2021 Steve Njuguna

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
