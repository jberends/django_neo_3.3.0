# INSTALLATION

To install and make it work follow this

## when using pipenv 
On the bash shell do:

 * `pipenv install --three`
 * `pipenv shell`
 
## when using pip
On the bash shell: 

 * `virtualenv venv --python=python3`
 * `. venv/bin/activate`
 * `pip install -r requrements.txt`
 
## installing database
when you activated the virtual environment

 * `./manage.py migrate`
 * `./manage.py createsuperuser`
 * provide superuser name, email and pass
 * start the server with: `./manage.py runserver`
 * navigate to link provided in your favorite webbrowser: http://127.0.0.1:8000
 * to access admin environment: http://127.0.0.1:8000/admin

## installing labels for neomodel
in the activated virtual environment

 * `neomodel_install_labels neoworld/models.py --db bolt://neo4j:<PASSWORD>@localhost:7687`
