from os import name
from django.contrib import admin
from django.urls import path,include
from Main import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signUp,name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
