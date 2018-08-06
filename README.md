## python-gunicorn-bottle-skeleton

## Steps
```
# clone repo
git clone git@github.com:Pratilipi/python-gunicorn-bottle-skeleton.git

# create a new service
mv python-gunicorn-bottle-skeleton <<ecs-service-name>>

# change dir
cd <<ecs-service-name>>

# setup nginx
cp <<ecs-service-name>>/prerequisite/service.nginx /etc/nginx/sites-available/service
ln -s /etc/nginx/sites-available/service /etc/nginx/sites-enabled/

# setup virtualenv
virtualenv .venv
. .venv/bin/activate

# install requirments
pip install -r requirements.txt

# set db config
export MASTER_DB_ENDPOINT_RW=localhost
export MASTER_DB_PORT=3306
export MASTER_MYSQL_DB_USERNAME=root
export MASTER_MYSQL_DB_PASSWORD=root

# run gunicorn
gunicorn -c gunicorn_conf.py --reload wsgi

# check if service is running
curl -X GET http://localhost:8100/health
response : {"state": "healthy"}

# check if db connection is working
curl -X GET http://localhost:8100/pingdb
response : {"message": "2018-08-06 17:50:16"}
