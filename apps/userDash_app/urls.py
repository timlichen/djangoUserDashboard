from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'home' ),
    url(r'^login', views.login, name = 'login'),
    # url(r'^signin', views.signin, name = 'signin'),
    url(r'^wall/(?P<id>[0-9]+)$', views.wall, name = 'wall'),
    url(r'^register$', views.register, name = 'register'),
    url(r'^registerUser', views.registerUser, name = 'registerUser'),
    url(r'^admin', views.adminPanel, name = 'adminPanel'),
    url(r'^edit/(?P<id>[0-9]+)$', views.edit, name = 'edit'),
    url(r'^edit/$', views.edit, name = 'edit',),
    url(r'^remove/(?P<id>[0-9]+)$', views.remove, name = 'remove'),
    url(r'^edit/password/(?P<id>[0-9]+)$', views.change_pass, name = 'change_pass'),
    url(r'^edit/change_desc/(?P<id>[0-9]+)$', views.change_desc, name = 'change_desc'),
    url(r'^logout', views.logout, name='logout')
]
