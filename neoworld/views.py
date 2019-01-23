from django.http import HttpResponse

from .models import Person


def index(request):
    # access nemodel list of graph objects
    latest_persons = Person.nodes
    header = '<h1>List of nodes</h1>'
    output = ''.join(['<pre>{}</pre><br />'.format(p) for p in latest_persons])
    count = '<p>{} nodes</p>'.format(len(latest_persons))
    return HttpResponse(header+output+count)


def detail(request, person_id):
    return HttpResponse('Id {}'.format(person_id))
