from django.shortcuts import render,redirect
from .decorators import unauthenticated_user,role_required
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as Login
from django.contrib.auth import logout as Logout
from .models import User,Project

def home(request):
    user=request.user
    Projects = Project.objects.all()
    context={
        'user':user,
        'Projects': Projects,
    }
    return render(request,'Home.html',context)

@role_required(['Admin', 'Manager'])
def edit_project(request):
     if request.method == 'POST':
        project_id = request.POST.get('project_id')
        project_name = request.POST.get('project_name')
        project_image = request.FILES.get('project_image')
        project = Project.objects.get(id=project_id)
        print(project_id)
        print(project_name)
        print(project_image)
        
        project.project_name = project_name
        if project_image:
            project.project_image = project_image
            
        project.save()
        messages.success(request, "Project updated successfully.")
        return redirect('home')

@role_required((['Admin']))
def delete_project(request,project_id):
    if request.method == 'POST':
        try:
            project=Project.objects.get(id=project_id)
        except:
            messages.error('no project found')
        project.delete()  
        messages.success(request, "Project deleted successfully.")
        return redirect('home')
@role_required(['Admin', 'Manager'])
def add_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        project_image = request.FILES.get('project_image')

        Project.objects.create(
            project_name=project_name,
            project_image=project_image
        )
        
        messages.success(request, "Project added successfully.")
        return redirect('home')



@unauthenticated_user
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                Login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('home') 
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Form is not valid.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')  
        else:
            print(form.errors)
            messages.error(request, "There were errors in your submission.")
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def logout(request):
    Logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')

