from django.contrib import admin
from . import models

admin.site.register(models.Document)
admin.site.register(models.Tag)
admin.site.register(models.Portfolio)