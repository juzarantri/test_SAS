from os import name
from django.contrib import admin
from django.urls import path,include
from Main import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.registration_view,name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('teacher/',views.teacher_registration_view,name ="teacher"),
    path('start_stop/',views.start_stop,name ="start_stop")
]
