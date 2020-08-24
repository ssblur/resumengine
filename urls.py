from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='portfolio-index'),
    path('search', views.search, name='portfolio-search'),
    path('document/<id>', views.document, name='portfolio-document'),
    path('tag/<name>', views.tag, name='portfolio-tag')
]