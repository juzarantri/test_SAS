from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    def get(self,request,**kwargs):
        return render(request,'index.html')
def aboutMe(request):
    return render(request,'AboutMe.html')
def contactMe(request):
    return render(request,'ContactMe.html')
