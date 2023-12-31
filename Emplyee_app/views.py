from contextlib import ContextDecorator
from datetime import datetime
from email import message
from django.db.models import Q
from django.shortcuts import render,HttpResponse,redirect
from .models import Employee,Role,Department
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse



from Emplyee_app.models import Employee

def login_page(request):

    if request.method == 'POST':
        user_name = request.POST['user_name']
        password1 = request.POST['password1']
        user = authenticate(username = user_name,password = password1)

        if user is not None:
            login(request,user)
            first_name = user.first_name
            last_name = user.last_name
            return render(request,"index.html",{'first_name':first_name,'last_name':last_name})
        else:
            messages.error(request,"bad credentials")
            return redirect('login_page')

    return render(request,"login_page.html")


# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')
    
@login_required
def all_emp(request):
    emp = Employee.objects.all()
    context = {
        'emp': emp
    }
    return render(request,'all_emp.html',context)

@login_required
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept, role_id = role, hire_date=datetime.now())
        new_emp.save()

       
        return redirect('emp_added_success')
       
    elif request.method == 'GET':   
        return render(request,'add_emp.html')
    else:
        return HttpResponse("an exception occured! Employee not added")
@login_required
def emp_added_success(request):
    return render(request, 'emp_added_success.html') 


@login_required
def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
         
            return redirect('emp_removed_success')

        except:
            return HttpResponse("Please enter a valid employee id")


    emp1 = Employee.objects.all();
    context = {
        'emp1':emp1
    }

    return render(request,'remove_emp.html',context)
@login_required
def emp_removed_success(request):
    return render(request, 'emp_removed_success.html') 

@login_required  
def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        dept = request.POST['dept']

        emp = Employee.objects.all()

        if name:
            emp = emp.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emp = emp.filter(dept__name__icontains = dept)
        if role:
            emp = emp.filter(role__name__icontains = role)
        context = {
            'emp':emp
        }
        return render(request,'all_emp.html',context)
    elif request.method == 'GET':  
        return render(request,'filter_emp.html')

    else:
        return HttpResponse("An error occured")
@login_required
def signout(request):
    logout(request)
    messages.success(request,"Logged out succesfully")
    return redirect('login_page')

@login_required
def About(request):
    return render(request,'About.html')

@login_required
def Contact(request):
    if request.method == 'POST':
    
        message = request.POST.get('queries', '')

        sender_email = 'devprince4723@gmail.com'
        recipient_email = 'pandeyprince4723@gmail.com'
        subject = 'New Contact Form Submission'

        send_mail(subject, message, sender_email, [recipient_email])

        return HttpResponseRedirect(reverse('Mail_sent'))  
    return render(request,'Contact.html')


@login_required
def Mail_sent(request):
    return render(request,"Mail_sent.html")