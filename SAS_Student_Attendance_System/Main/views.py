from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def home(request):
    count = User.objects.count()
    return render(request,'home.html',{
        'count':count
    })

def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{
        'form':form
    })
