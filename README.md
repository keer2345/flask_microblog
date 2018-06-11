**Catalog:**


<!-- vim-markdown-toc GFM -->

* [Welcome to Microblog!](#welcome-to-microblog)
    * [Enviroment](#enviroment)
    * [Database](#database)
        * [With Flask-Script](#with-flask-script)
        * [With Flask-CLI](#with-flask-cli)
* [Deploy](#deploy)
* [Docker Usage](#docker-usage)
    * [Access our Container:](#access-our-container)
    * [Management Docker's container:](#management-dockers-container)
    * [Management Docker's images:](#management-dockers-images)
    * [Access PostgreSQL:](#access-postgresql)

<!-- vim-markdown-toc -->

# Welcome to Microblog!

This is an example application featured in my [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). See the tutorial for instructions on how to work with it.

## Enviroment
- virtualenv
- pip install -r requirements.txt (*pip freeze > requirements.txt*)
- python microblog.py runserver


## Database
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

docker-compose -f docker-compose-dev.yml up -d --build
```

# Docker Usage
## Access our Container:
```
docker container ls -a
docker exec -it [CONTAINER ID] /bin/bash
```

## Management Docker's container:
```
docker ps
docker ps -a

docker stop [CONTAINER ID]
docker rm [CONTAINER ID]
docker rm $(docker ps -a -q -f status=exited)
```
## Management Docker's images:
```
docker images
docker rmi [IMAGE ID]
docker rmi $(docker images | grep "none" | awk '{print $3}')
```

## Access PostgreSQL:
```
docker exec -ti $(docker ps -aqf "name=microblog-db") psql -U postgres
```

Example:
```
$ docker exec -ti $(docker ps -aqf "name=microblog-db") psql -U postgres

psql (10.4 (Debian 10.4-2.pgdg90+1))
Type "help" for help.

postgres=# \c microblog
You are now connected to database "microblog" as user "postgres".
microblog=# \dt
              List of relations
 Schema |      Name       | Type  |  Owner   
--------+-----------------+-------+----------
 public | alembic_version | table | postgres
 public | followers       | table | postgres
 public | post            | table | postgres
 public | users           | table | postgres
(4 rows)

microblog=# select * from users;
 id | username | email | password_hash | about_me | last_seen 
----+----------+-------+---------------+----------+-----------
(0 rows)

microblog=# 
```
