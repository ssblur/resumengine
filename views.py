from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import SearchForm
from .models import Document, Tag, Portfolio, PortfolioAlias
from .forms import SearchForm

index_template = loader.get_template('index.django-html')
def index(req):
    '''
    The index page for portfolios.
    This indexes the most recent 20 documents, most recent first.
    '''
    docs = Document.objects.order_by('last_updated')[:20]
    return HttpResponse(index_template.render(
        {
            'documents': docs
        },
        req
    ))

search_template = loader.get_template('search.django-html')
def search(req):
    'A handler for searching based on tags, description, and name.'
    if req.method == 'GET':
        form = SearchForm(req.GET)
    elif req.method == 'POST':
        form = SearchForm(req.POST)
    else:
        form = SearchForm()
    if form.is_valid():
        q = form.cleaned_data['q']
        docs = Document.search(q)
        return HttpResponse(search_template.render(
            {
                'documents': docs,
                'q': q,
                'search': SearchForm
            },
            req
        ))
    else:
        return HttpResponse('Invalid Search Term!')
        
document_template = loader.get_template('solo-documents.django-html')
no_document_template = loader.get_template('solo-documents-404.django-html')
def document(req, id):
    '''
    Renders a single document onto its own page.
    @param id The document id to look up.
    '''
    try:
        doc = Document.objects.get(id = int(id))
        return HttpResponse(document_template.render(
            {
                'document': doc,
                'search': SearchForm
            },
            req
        ))
    except Exception:
        return HttpResponse(no_document_template.render(
            {
                'id': id,
                'search': SearchForm
            },
            req
        ))

tag_documents = loader.get_template('tag-documents.django-html')
def tag(req, name):
    docs = Document.objects.filter(tags__tag_name = name)
    output = ''
    return HttpResponse(tag_documents.render(
        {
            'documents': docs,
            'search': SearchForm,
            'tag': name
        },
        req
    ))

portfolio_template = loader.get_template('portfolio.django-html')
no_portfolio_template = loader.get_template('portfolio-404.django-html')
def portfolio(req, id):
    'Renders a portfolio and its component documents.'
    try:
        portfolio = Portfolio.objects.get(uuid = id)
        return HttpResponse(portfolio_template.render(
            {
                'portfolio': portfolio,
            },
            req
        ))
    except Exception:
        try:
            alias = PortfolioAlias.objects.get(name = id)
            portfolio = alias.target
            return HttpResponse(portfolio_template.render(
                {
                    'portfolio': portfolio,
                },
                req
            ))
        except Exception as e:
            return HttpResponse(no_portfolio_template.render(
                {
                    'id': id,
                    'search': SearchForm
                },
                req
            ))