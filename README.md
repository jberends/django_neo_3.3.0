# DJANGO SCAFFOLD

This is a django scaffold with an SQL based model and a neomodel graph model.
It is made to zoom in on the problem in neomodel between the versions 3.2.9 and 3.3.0 in combination with django.

It is made to support issue https://github.com/neo4j-contrib/neomodel/issues/378

# INSTALLATION

To install and make it work follow this

## When using pipenv 
On the bash shell do:

 * `pipenv install --three`
 * `pipenv shell`
 
## When using pip
On the bash shell: 

 * `virtualenv venv --python=python3`
 * `. venv/bin/activate`
 * `pip install -r requrements.txt`
 
## Installing database
When you activated the virtual environment

 * `./manage.py migrate`
 * `./manage.py createsuperuser`
 * provide superuser name, email and pass
 * start the server with: `./manage.py runserver`
 * navigate to link provided in your favorite webbrowser: http://127.0.0.1:8000
 * to access admin environment: http://127.0.0.1:8000/admin

## Installing labels for neomodel
In the activated virtual environment.

 * `neomodel_install_labels neoworld/models.py --db bolt://neo4j:<PASSWORD>@localhost:7687`

## Switch between neomodel versions
Depends if you use pip or pipenv, alter the `requirements.txt` (for pip) or `Pipfile` to switch to different version of neomodel. 

## Error when using neomodel 3.3.0

 * switch to neomodel version 3.3.0
 * restart the server
 * ensure you already have some models loaded
 * list all person objects using:  

```
[24/Jan/2019 12:32:42] "GET / HTTP/1.1" 200 1676
Internal Server Error: /persons/
Traceback (most recent call last):
  File "~/.local/share/virtualenvs/django_neo_3.3.0-F55v51Sh/lib/python3.6/site-packages/neomodel/util.py", line 150, in _object_resolution
    resolved_object = self._NODE_CLASS_REGISTRY[frozenset(a_result_attribute[1].labels)].inflate(
KeyError: frozenset({'Person'})

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "~/.local/share/virtualenvs/django_neo_3.3.0-F55v51Sh/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "~/.local/share/virtualenvs/django_neo_3.3.0-F55v51Sh/lib/python3.6/site-packages/django/core/handlers/base.py", line 126, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "~/.local/share/virtualenvs/django_neo_3.3.0-F55v51Sh/lib/python3.6/site-packages/django/core/handlers/base.py", line 124, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "~/dev/django_neo_3.3.0/neoworld/views.py", line 18, in index
    latest_persons = Person.nodes.all()
  File "~/.local/share/virtualenvs/django_neo_3.3.0-F55v51Sh/lib/python3.6/site-packages/neomodel/match.py", line 469, in all
    return self.query_cls(self).build_ast()._execute()
  File "~/.local/share/virtualenvs/django_neo_3.3.0-F55v51Sh/lib/python3.6/site-packages/neomodel/match.py", line 445, in _execute
    results, _ = db.cypher_query(query, self._query_params, resolve_objects=True)
  File "~/.local/share/virtualenvs/django_neo_3.3.0-F55v51Sh/lib/python3.6/site-packages/neomodel/util.py", line 32, in wrapper
    return func(self, *args, **kwargs)
  File "~/.local/share/virtualenvs/django_neo_3.3.0-F55v51Sh/lib/python3.6/site-packages/neomodel/util.py", line 202, in cypher_query
    results = self._object_resolution(results)
  File "~/.local/share/virtualenvs/django_neo_3.3.0-F55v51Sh/lib/python3.6/site-packages/neomodel/util.py", line 162, in _object_resolution
    raise ModelDefinitionMismatch(a_result_attribute[1], self._NODE_CLASS_REGISTRY)
neomodel.exceptions.ModelDefinitionMismatch: Node with labels Person does not resolve to any of the known objects

```

# Credits

* @jberends / Jan 2019
