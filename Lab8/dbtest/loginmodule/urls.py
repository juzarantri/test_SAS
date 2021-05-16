from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls.resolvers import URLPattern
#from loginmodule.views import login, auth_view, logout,loggedin, invalidlogin
from . import views
urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^auth/$',views.auth_view),
    url(r'^logout/$',views.logout),
    url(r'^loggedin/$',views.loggedin),
    url(r'^invalidlogin/$',views.invalidlogin),
]