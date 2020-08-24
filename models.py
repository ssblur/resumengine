from django.db import models
from django.template import loader
from django.db.models import Q

# Document visibility enumeration.
Visibility = models.IntegerChoices('Visibility', 'PUBLIC PROTECTED PRIVATE')

# A document type enumeration, for sorting different varieties of document.
ProjectType = models.IntegerChoices('ProjectType', 'PROJECT EDUCATION AWARD EXPERIENCE')


class Tag(models.Model):
    'A tag which can be attributed to documents, on a many-to-one basis.'
    tag_name = models.CharField(max_length = 32)
    def __str__(self):
        return self.tag_name

class Document(models.Model):
    '''
    A representation of input Documents.
    These could be portfolio pieces, education, or other media for representing the user.
    '''
    document_name = models.CharField(max_length = 128)
    document_type = models.IntegerField(choices = ProjectType.choices)
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
    def __str__(self):
        return 'Portfolio for ' + str(self.recipient)
    def education(self):
        return self.documents.filter(document_type = ProjectType.EDUCATION)
    def project(self):
        return self.documents.filter(document_type = ProjectType.PROJECT)
    def award(self):
        return self.documents.filter(document_type = ProjectType.AWARD)
    def experience(self):
        return self.documents.filter(document_type = ProjectType.EXPERIENCE)
