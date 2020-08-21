from django.shortcuts import render
from django.http import HttpResponse

from .forms import SearchForm
from .models import Document, Tag

def index(req):
    'The index page for portfolios.'
    return HttpResponse('OK')

def search(req):
    if req.method == 'GET':
        form = SearchForm(req.GET)
    elif req.method == 'POST':
        form = SearchForm(req.POST)
    else:
        form = SearchForm()
    if form.is_valid():
        return HttpResponse(form.cleaned_data['q']) #TODO
    else:
        return HttpResponse('Invalid Search Term!') #TODO

def document(req, id):
    doc = Document.objects.get(id = int(id))
    return HttpResponse(str(doc))

def tag(req, name):
    docs = Document.objects.filter(tags__tag_name = name)
    output = ''
    for i in docs:
        output += str(i) + '<br>'
    return HttpResponse(output)