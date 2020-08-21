from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('document/<id>', views.document, name='document'),
    path('tag/<name>', views.tag, name='tag')
]