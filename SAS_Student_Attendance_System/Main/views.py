from os import error
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .models import Student,Teacher
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import django.utils.timezone as timezone
from django.contrib.auth.decorators import login_required

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
                return redirect('/?id=1')
        else:
            return render(request,'registration/teacher_signup.html',{
            'error': "Password Don't Match"
            })
    else:
        return render(request,'registration/teacher_signup.html')

# Attendance start stop page
@login_required(login_url='')
def start_stop(request):
    return render(request,'attendance/start_stop.html')

# # starting attendance
@login_required(login_url='')
def startAttendance(request):
    if request.method == 'POST':
        branch = request.POST['branch']
        semester = request.POST['sem']
        subject = request.POST['subject']
        teacher = request.POST['teacher']
        tblname = branch+"_"+semester+"_"+subject+"_"+str(timezone.now().year)
        error = []
        error = []
        if branch == '':
            error.append("Branch must not be empty")
        if semester == "Select the semester":
            error.append("Please choose valid semester")
        if subject == '':
            error.append("Subject must not be empty")
        if error:
            return render(request,'attendance/start_stop.html',{
            'error': error
            })
        else:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS attendance_start_stop (branch VARCHAR(50), semester VARCHAR(50), subject VARCHAR(50), status INT, tableName VARCHAR(50), faculty VARCHAR(50));")
            cursor.execute("SELECT * FROM attendance_start_stop WHERE tableName = '"+tblname+"' AND faculty = '"+teacher+"';")
            if cursor.fetchall():
                cursor.execute("CREATE TABLE IF NOT EXISTS "+tblname+" (name VARCHAR(50), student_id VARCHAR(50), roll_no VARCHAR(50), present INT, date DATE);")
                sql = "UPDATE attendance_start_stop SET status = 1 WHERE tableName = '"+tblname+"';"
                cursor.execute("SELECT tableName FROM attendance_start_stop WHERE faculty = '"+teacher+"' AND status = 1 ;")
                on_going_attendance = cursor.fetchall()
                cursor.execute(sql)
            else:
                cursor.execute("CREATE TABLE IF NOT EXISTS "+tblname+" (name VARCHAR(50), student_id VARCHAR(50), roll_no VARCHAR(50), present INT, date DATE);")
                sql = "INSERT INTO attendance_start_stop VALUES(%s,%s,%s,%s,%s,%s);"

                val = (branch,semester,subject,1,tblname,teacher)
                cursor.execute(sql,val)
                cursor.execute("SELECT tableName FROM attendance_start_stop WHERE faculty = '"+teacher+"' AND status = 1 ;")
                on_going_attendance = cursor.fetchall()
            return render(request,'attendance/start_stop.html',{
                'message':"Attendance for "+branch+" "+semester+" "+subject+" has been started",
                'on_going_attendance':on_going_attendance
            })
    else:
        return render(request,'attendance/start_stop.html')

# stopping attendance
@login_required(login_url='')
def stopAttendance(request,table):
        # table = table
        # s = ""
        # for t in range(len(table)):
        #     if table[t] == '(' or table[t] == ')' or table[t] == ',' or table[t] == "'" :
        #         pass
        #     else:
        #         s += table[t]
        # table = s
        error = []
        error.append("table")
        return render(request,'attendance/start_stop.html',{
                # 'on_going_attendance': on_going_attendance,
                'error':error,
        })
        
        # cursor = connection.cursor()
        # # cursor.execute("SELECT tableName FROM attendance_start_stop WHERE tableName = '"+table+"';")
        # if cursor.fetchall():
        #     error = []
        #     cursor = connection.cursor()
        #     # sql = "UPDATE attendance_start_stop SET status = 0 WHERE tableName = '"+table+"';"        
        #     # cursor.execute(sql)
        #     # cursor.execute("SELECT tableName FROM attendance_start_stop WHERE faculty = '"+teacher+"' AND status = 1 ;")
        #     # on_going_attendance = cursor.fetchall()
        #     error.append(table)
        #     return render(request,'attendance/start_stop.html',{
        #         # 'on_going_attendance': on_going_attendance,
        #         'error':error,
        #     })
        # else:
        #     # cursor.execute("SELECT tableName FROM attendance_start_stop WHERE faculty = '"+teacher+"' AND status = 1 ;")
        #     # on_going_attendance = cursor.fetchall()
        #     error = []
        #     error.append("Error while stopping attendance")
        #     return render(request,'attendance/start_stop.html',{
        #         'error': error,
        #         # 'on_going_attendance':on_going_attendance,
        #     })

#refreshing table
@login_required(login_url='')
def refreshAttendanceTable(request,teacher):
    teacher = teacher
    cursor = connection.cursor()
    cursor.execute("SELECT tableName FROM attendance_start_stop WHERE faculty = '"+"teacher1"+"' AND status=1 ;")
    on_going_attendance = cursor.fetchall()
    if on_going_attendance:
        return render(request,'attendance/start_stop.html',{
        'on_going_attendance': on_going_attendance,
    })
    else:
        error = []
        error.append("No Record Found")
        return render(request,'attendance/start_stop.html',{
            'error': error,
        })
