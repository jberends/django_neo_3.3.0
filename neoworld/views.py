from random import randint

from django.http import HttpResponse
from faker import Faker

from .models import Person

TEMPLATE = """
<h1>{title}</h1>

<p>{message}</p>
<p>{footer}</p>
"""


def index(request):
    # access nemodel list of graph objects
    latest_persons = Person.nodes.all()
    context = dict(
        title='List of nodes',
        message=''.join(['<pre>{}</pre><br />'.format(p) for p in latest_persons]),
        footer='{} nodes'.format(len(latest_persons))
    )
    return HttpResponse(TEMPLATE.format(**context))


def detail(request, person_id):
    return HttpResponse('Id {}'.format(person_id))


def create(request):
    new_person = Person(name=Faker().name(), age=randint(0, 88))
    new_person.save()
    context = dict(
        title="created new Person",
        message="name = {name}, age = {age}".format(name=new_person.name, age=new_person.age),
        footer=""
    )

    return HttpResponse(TEMPLATE.format(**context))
