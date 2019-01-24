import os

from django.http import HttpResponse

HOMEPAGE = """
<html><body>
<h1>Home</h1>

<h2>List of links</h2>
<p><a href="/persons">/persons - List persons</a><p>
<p><a href="/persons/create">/persons/create - Create a new person</a><p>
<p><a href="http://localhost:7474" target="_new">open noe4j browser in other page</a><p>

<h2>Installation</h2>
<pre>{installation_text}</pre>
</body>
</html>
"""

def home(request):
    """Homepage"""

    # inject installation text here
    with open(os.path.join(os.path.dirname(__file__),'../README.md')) as fd:
        installation_text = fd.read()

    return HttpResponse(HOMEPAGE.format(installation_text=installation_text))
