# Welcome to Microblog!

This is an example application featured in my [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). See the tutorial for instructions on how to work with it.

## Enviroment
- virtualenv
- pip install -r requirements.txt (*pip freeze > requirements.txt*)
- python microblog.py runserver


## **Database**
```
python microblog.py db init
python microblog.py db migrate -m "login support"
python microblog.py db upgrade
```


# Deploy
Example:
```
docker-compose -f docker-compose-dev.yml build
docker-compose -f docker-compose-dev.yml up -d
```
