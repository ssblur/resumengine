from django.db import models
from django.template import loader

Visibility = models.IntegerChoices('Visibility', 'PUBLIC PROTECTED PRIVATE')
ProjectType = models.IntegerChoices('ProjectType', 'PROJECT EDUCATION AWARD EXPERIENCE')
'''
An enumeration for document visibility.
May be used for other things in the future, so not a field in Document.
'''

class Tag(models.Model):
    '''
    A tag which can be attributed to documents, on a many-to-one basis.
    '''
    tag_name = models.CharField(max_length = 32)
    def __str__(self):
        return self.tag_name

document_template = loader.get_template('document.django-html')
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
    since = models.DateField()
    visibility = models.IntegerField(choices = Visibility.choices)
    tags = models.ManyToManyField(Tag, blank = True, null = True)
    def __str__(self):
        return self.document_name

class Portfolio(models.Model):
    '''
    A representation of a portfolio that can be sent to individual users.
    '''
    recipient = models.TextField()
    description = models.TextField()
    icon = models.ImageField(upload_to = 'icons', blank=True, null=True)
    documents = models.ManyToManyField(Document)
    def __str__(self):
        return 'Document for ' + str(self.recipient)