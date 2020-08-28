from django.contrib import admin
from . import models

# Registering the models we intend to use.
admin.site.register(models.Document)
admin.site.register(models.Tag)
admin.site.register(models.Portfolio)
admin.site.register(models.PortfolioAlias)
admin.site.register(models.DocumentCategory)