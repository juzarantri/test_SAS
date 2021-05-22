from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from .models import Student

def getStudentInfo(request):
    c = {}
    c.update(csrf(request))
    return render(request,"addStudentInfo.html",c)  

def addStudentInfo(request):
    sname = request.POST.get('studentname','')
    sdate = request.POST.get('birthdate','')
    s = Student(student_name = sname,student_dob = sdate)
    s.save()
    return HttpResponseRedirect('/dbtest/addsuccess')

def addsuccess(request):
    return render(request,'addrecord.html')

class StudentListView(generic.ListView):
    model = Student