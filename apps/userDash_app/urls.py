from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'home' ),
    url(r'^login', views.login, name = 'login'),
    url(r'^signin', views.signin, name = 'signin'),
    url(r'^register$', views.register, name = 'register'),
    url(r'^registerUser', views.registerUser, name = 'registerUser'),
    url(r'^admin', views.adminPanel, name = 'adminPanel'),
    url(r'^edit/(?P<id>[0-9]+)$', views.edit, name = 'edit'),
    url(r'^remove/(?P<id>[0-9]+)$', views.remove, name = 'remove')
]
