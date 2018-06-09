FROM python

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

# add app
COPY . /usr/src/app

# run server
CMD ["python", "manage.py"]
