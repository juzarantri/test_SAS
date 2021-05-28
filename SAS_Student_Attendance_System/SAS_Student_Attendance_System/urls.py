from os import name
from django.contrib import admin
from django.urls import path,include,re_path
from Main import views
from django.conf.urls import url
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.registration_view,name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('teacher/',views.teacher_registration_view,name ="teacher"),
    path('start_stop/',views.start_stop,name ="start_stop"),
    re_path('start_attendance/',views.startAttendance,name ="start_attendance"),
    url(r'^make_attendance/$',views.makeAttendance,name ="make_attendance"),
    url(r'^stop_attendance/(?P<table>\w+)/(?P<teacher>\w+)/$',views.stopAttendance,name="stop_attendance"),
    url(r'^refreshAttendanceTable/(?P<teacher>\w+)/$',views.refreshAttendanceTable,name="refreshAttendanceTable"),
    url(r'^refreshStudentAttendanceTable/(?P<username>\w+)/$',views.refreshStudentAttendanceTable,name="refreshStudentAttendanceTable"),
    url(r'^clickedPresent/(?P<table>\w+)/(?P<student>\w+)/$',views.clickedPresent,name="clickedPresent")
]
