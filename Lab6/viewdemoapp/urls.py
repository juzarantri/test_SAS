from viewdemoapp import views
from django.conf.urls import url
urlpatterns = [
    url(r'^index/$',views.HomePage.as_view()),
    url(r'^aboutme/$',views.aboutMe),
    url(r'^contactme/$',views.contactMe),
]