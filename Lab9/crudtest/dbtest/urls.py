from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addStudentInfo/$',views.addStudentInfo),
    url(r'^getStudentInfo/$',views.getStudentInfo),
    url(r'^addsuccess/$',views.addsuccess),
    url('students/',views.StudentListView.as_view(),name='students'),
]