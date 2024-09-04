from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Doctor,Patient,Operation, Nurse, Nurse_List
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import DoctorForm, OperationForm, PatientForm, NurseForm, Nurse_ListForm
from .decorators import unauthenticated_user, allowed_users, admin_only

#***********************************************************************************************************************
@unauthenticated_user
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            group = Group.objects.get(name ='doctor')
            my_user.groups.add(group)
            return redirect('Login_Page')
        

    return render (request,'signuppage.html')


@unauthenticated_user
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'loginpage.html')



def LogoutPage(request):
    if User is None:

        return redirect('login')

    logout(request)
    return redirect('Login_Page')

#***********************************************************************************************************************
def About(request):
    return render(request,'about.html')

def Logout_Home(request):
    return render(request, 'logout_home.html')

@admin_only
def Home(request):
    return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')

@allowed_users(allowed_roles=['admin','doctor','nurse_admin','nurse'])
def Index(request):
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    operation = Operation.objects.all()
    nurse = Nurse.objects.all()
    nurse_list = Nurse_List.objects.all()
    d=0
    P=0
    a=0
    n=0
    nl=0
    for i in doctors:
        d +=1
    for i in patient:
        P +=1
    for i in operation:
        a +=1
    for i in nurse:
        n +=1
    for i in nurse_list:
        nl +=1        
    d1 = {'d' : d, 'p': P, 'a': a, 'n' : n, 'nl' : nl}
    return render(request, 'index.html', d1)

#***********************************************************************************************************************
@allowed_users(allowed_roles=['admin','doctor'])
def Add_Doc(request):
    submitted = False
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_doc?submitted=True')
    else:
        form = DoctorForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'doctor_form.html', {'form':form, 'submitted':submitted})

@allowed_users(allowed_roles=['admin','doctor'])
def  View_Doctor(request):
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request, 'view_doctor.html', d)

@allowed_users(allowed_roles=['admin','doctor'])
def  Delete_Doctor(request,pid):
    doctor = Doctor.objects.get(id = pid)
    doctor.delete()
    return redirect('view_doctor')

#***********************************************************************************************************************


@allowed_users(allowed_roles=['admin','doctor'])
def Add_Pat(request):
    submitted = False
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_pat?submitted=True')
    else:
        form = PatientForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'patient_form.html', {'form':form, 'submitted':submitted})

@allowed_users(allowed_roles=['admin','doctor'])
def  View_Patient(request):
    doc = Patient.objects.all()
    d = {'doc':doc}
    return render(request, 'view_patient.html', d)

@allowed_users(allowed_roles=['admin','doctor'])
def  Delete_Patient(request,pid):
    patient = Patient.objects.get(id = pid)
    patient.delete()
    return redirect('view_patient')

#***********************************************************************************************************************
@allowed_users(allowed_roles=['admin','nurse_admin'])
def Add_Nurse(request):
    submitted = False
    if request.method == "POST":
        form = NurseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_nurse?submitted=True')
    else:
        form = NurseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'nurse_form.html', {'form':form, 'submitted':submitted})

@allowed_users(allowed_roles=['admin','doctor', 'nurse_admin','nurse'])
def  View_Nurse(request):
    doc = Nurse.objects.all()
    d = {'doc':doc}
    return render(request, 'view_nurse.html', d)

@allowed_users(allowed_roles=['admin','nurse_admin'])
def  Delete_Nurse(request,pid):
    nurse = Nurse.objects.get(id = pid)
    nurse.delete()
    return redirect('view_nurse')

#***********************************************************************************************************************



@allowed_users(allowed_roles=['admin','doctor'])
def Add_Oper(request):
    submitted = False
    if request.method == "POST":
        form = OperationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_oper?submitted=True')
    else:
        form = OperationForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'operation_form.html', {'form':form, 'submitted':submitted})

@allowed_users(allowed_roles=['admin','doctor','nurse_admin'])
def  View_Operation(request):
    doc = Operation.objects.all()
    d = {'doc':doc}
    return render(request, 'view_operation.html', d)

@allowed_users(allowed_roles=['admin','doctor', 'nurse_admin'])
def  Delete_Operation(request,pid):
    operation = Operation.objects.get(id=pid)
    operation.delete()
    return redirect('view_operation')

#***********************************************************************************************************************

@allowed_users(allowed_roles=['admin','nurse_admin'])
def Add_Nurse_List(request):
    submitted = False
    if request.method == "POST":
        form = Nurse_ListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_nurse_list?submitted=True')
    else:
        form = Nurse_ListForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'nurse_list_form.html', {'form':form, 'submitted':submitted})

@allowed_users(allowed_roles=['admin','doctor','nurse_admin','nurse'])
def  View_Nurse_List(request):
    doc = Nurse_List.objects.all()
    d = {'doc':doc}
    return render(request, 'view_nurse_list.html', d)

@allowed_users(allowed_roles=['admin','nurse_admin'])
def  Delete_Nurse_List(request,pid):
    nurse_list = Nurse_List.objects.get(id=pid)
    nurse_list.delete()
    return redirect('view_nurse_list')

#***********************************************************************************************************************





































def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(request, username=u, password=p)
        #print(user.is_staff)
        print("============================")
        try:
            
            if user is not None and user.is_doctor:    
                login(request, user)
                return HttpResponseRedirect(reverse("dashboard"))
            
            else:
                error = "yes"

        except:
            error = "yes"
        d = {'error': error}
        return render(request, 'login.html', d)
    return render(request, 'login.html')

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('admin_login')




def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']
        try:
            Doctor.objects.create(Name=n, mobile=m, special=sp)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_doctor.html', d)



def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, address=a)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_patient.html', d)



def Add_Operation(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == "POST":
        n = request.POST['doctor']
        p = request.POST['patient']
        de = request.POST['department']
        da = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(Name=n).first()
        patient = Patient.objects.filter(name=p).first()
        
        # try:
        print(n, p, da, t)
        print("==========================")
        Operation.objects.create(doctor=doctor, patient=patient, department=de, date=da, time=t)
        error = "no"
        # except:
        #     error = "yes"
    d = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, 'add_operation.html', d)



