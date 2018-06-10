# Welcome to Microblog!

This is an example application featured in my [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). See the tutorial for instructions on how to work with it.

## Enviroment
- virtualenv
- pip install -r requirements.txt (*pip freeze > requirements.txt*)
- python microblog.py runserver


## **Database**
### With Flask-Script
```
python microblog.py db init
python microblog.py db migrate -m "login support"
python microblog.py db upgrade
```

### With Flask-CLI
```
export FLASK_APP=manage.py
flask db init                        # create the migration repository
flask db migrate -m "users table"    # generates these automatic migrations
flask db upgrade                     # to apply the changes to the database
```


# Deploy
Example:
```
docker-compose -f docker-compose-dev.yml build
docker-compose -f docker-compose-dev.yml up -d
```

Access our Container:
```
docker container ls -a
docker exec -it [CONTAINER ID] /bin/bash
```
