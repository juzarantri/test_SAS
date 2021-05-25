from django.contrib.auth import login,authenticate
from django.shortcuts import redirect, render
from .models import Student,Teacher
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# home page
def home(request):
    count = Student.objects.count()
    return render(request,'home.html',{
        'count':count
    })

# student registration page
@csrf_exempt
def registration_view(request):
    if request.method == 'POST':
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                error = []
                User.objects.get(username=request.POST['uname'])
                error.append("Username has already been taken")
                Student.objects.get(phone_no=request.POST['phone_no'])
                error.append("Phone NO. must be unique")
                Student.objects.get(student_id=request.POST['student_id'])
                error.append("Student id must be unique")
                Student.objects.get(roll_no=request.POST['roll_no'])
                error.append("Roll NO. must be unique")
                return render(request,'registration/signup.html',{
                'error': error
                })
            except User.DoesNotExist:
                username = request.POST['uname']
                email = request.POST['email']
                user = User.objects.create_user(username = username,password = request.POST['pass1'],email = email)
                fullname = request.POST['fullname'] 
                phone_no = request.POST['phone_no']
                parent_phone_no = request.POST['parent_phone_no']
                branch = request.POST['branch']
                student_id = request.POST['student_id']
                roll_no = request.POST['roll_no']
                newStudent = Student(username = username,
                                          fullname = fullname,
                                          phone_no = phone_no,
                                          parents_phone_no = parent_phone_no,
                                          branch = branch,
                                          student_id = student_id,
                                          roll_no = roll_no,
                                          user = user)
                newStudent.save()
                login(request,user)
                return redirect('home')
        else:
            return render(request,'registration/signup.html',{
            'error': "Password Don't Match"
            })
    else:
        return render(request,'registration/signup.html')

# teacher registration page
def teacher_registration_view(request):
    if request.method == 'POST':
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                User.objects.get(username=request.POST['uname'])
                return render(request,'registration/teacher_signup.html',{
                'error': "Username has already been taken"
                })
            except User.DoesNotExist:
                username = request.POST['uname']
                email = request.POST['email']
                user = User.objects.create_user(username = username,password = request.POST['pass1'],email = email,is_staff = True)
                
                fullname = request.POST['fullname'] 
                phone_no = request.POST['phone_no']
                newTeacher = Teacher(username = username,
                                          fullname = fullname,
                                          phone_no = phone_no,
                                          user = user)
                newTeacher.save()
                login(request,user)
                return redirect('home')
        else:
            return render(request,'registration/teacher_signup.html',{
            'error': "Password Don't Match"
            })
    else:
        return render(request,'registration/teacher_signup.html')

# Attendance start stop page
def start_stop(request):
    return render(request,'attendance/start_stop.html')