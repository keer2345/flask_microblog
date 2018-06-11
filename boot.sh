#!/bin/sh

set -e

echo "Waiting for postgres..."

while ! nc -z microblog-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# flask db init
# flask db migrate
flask db upgrade

exec gunicorn -b :5000 --access-logfile - --error-logfile - manage:app

# this bash script checks port number 5432 of container named microblog-db
# to ascertain that it is open. this means that the postgres server is up and running
# microblog-db is what i named the postgres database container.
# when the port is open, then the script run all other subsequent commands following
# which commands are essentially running migrations on the database in that said container
# and then start the flask API application.
