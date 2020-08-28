from django.db import models
from django.template import loader
from django.db.models import Q
from uuid import uuid1

# Document visibility enumeration.
Visibility = models.IntegerChoices('Visibility', 'PUBLIC PROTECTED PRIVATE')


class Tag(models.Model):
    'A tag which can be attributed to documents, on a many-to-one basis.'
    tag_name = models.CharField(max_length = 32)
    def __str__(self):
        return self.tag_name

class DocumentCategory(models.Model):
    '''
    A category for documents.
    Replaces the previous enum.
    '''
    name = models.CharField(max_length = 32, unique = True)
    def __str__(self):
        return self.name

class Document(models.Model):
    '''
    A representation of input Documents.
    These could be portfolio pieces, education, or other media for representing the user.
    '''
    document_name = models.CharField(max_length = 128)
    document_type = models.ForeignKey(DocumentCategory, null = True, on_delete = models.PROTECT)
    contents = models.TextField()
    icon = models.ImageField(upload_to = 'icons', blank = True, null = True)
    last_updated = models.DateField(auto_now = True)
    created = models.DateField(auto_now_add = True)
    since = models.DateField(blank = True, null = True)
    until = models.DateField(blank = True, null = True)
    visibility = models.IntegerField(choices = Visibility.choices)
    tags = models.ManyToManyField(Tag, blank = True)
    def __str__(self):
        return self.document_name
    def search(q):
        return Document.objects.filter(
            Q(document_name__icontains = q) |
            Q(contents__icontains = q) |
            Q(tags__tag_name__icontains = q)
        ).distinct()

class Portfolio(models.Model):
    'A representation of a portfolio that can be sent to individual users.'
    recipient = models.TextField()
    description = models.TextField()
    icon = models.ImageField(upload_to = 'icons', blank=True, null=True)
    documents = models.ManyToManyField(Document)
    uuid = models.UUIDField(unique = True, default = uuid1, editable = False)
    def __str__(self):
        return 'Portfolio for ' + str(self.recipient)
    def categories(self):
        cats = DocumentCategory.objects.all()
        docs = []
        for category in cats:
            docs.append(Document.objects.filter(document_type = category))
        return zip(cats, docs)

class PortfolioAlias(models.Model):
    '''
    Aliases for portfolios.
    Useful as backwards compatibility for the old portfolio format, and for named URLs.
    '''
    name = models.CharField(max_length = 32, unique = True)
    target = models.ForeignKey(Portfolio, on_delete = models.CASCADE)
    def __str__(self):
        return 'Alias {} for {}'.format(self.name, self.target)