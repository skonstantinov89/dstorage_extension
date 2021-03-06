"""dstorage_extension URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from central_management.views import Central


urlpatterns = [
    # url(r'home$', ''''),
    url(r'preview$',        Central.preview.as_view(),  name='preview'),
    url(r'receipt$',        Central.receipt.as_view(),  name='receipt'),
    url(r'search$',         Central.search.as_view(),  name='search'),
    url(r'move-archive',    Central.moveToArchive.as_view(),  name='moveToArchive'),
    url(r'conformation',    Central.conformation.as_view(),  name='conformation'),
    url(r'$',               Central.Index.as_view(),    name='index')
]
