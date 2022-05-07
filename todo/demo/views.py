from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Task, Users, Login
from .models import User,Todo
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here

# This function will add the users
def add_users(request):
    if request.method == 'POST':
        us = Users(request.POST)
        if us.is_valid():
            n = us.cleaned_data['name']
            e = us.cleaned_data['email']
            p = us.cleaned_data['password']
            reg = User(name=n, email=e, password=p)
            reg.save()
            us = Users()
            fm1 = Login()
            return render(request,'demo/login.html', {'form':fm1})
    else:
        us = Users()
    return render(request,'demo/user.html', {'form':us})

# This function will verify the users
def authenticate(request):
    fm1 = Login()
    if request.method == 'POST':
        fm1 = Login(request.POST)
        try:
            email = request.POST['email']
            password = request.POST['password']
    
            user = User.objects.get(email=email, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                fm = Task()
                return render(request,'demo/add.html', {'form':fm, 'refresh': str(refresh),'access': str(refresh.access_token),'author':user.name, 'id':user.id})
    
                
            else:
                fm1 = Login()
                return render(request,'demo/login.html', {'form':fm1})
        except KeyError:
            fm1 = Login()
            return render(request,'demo/login.html', {'form':fm1})
    return render(request,'demo/login.html', {'form':fm1})

# This function add the items
def add(request,id):
    if request.method == 'POST':
        fm = Task(request.POST)
        if fm.is_valid():
            t = request.POST['task']
            i = request.POST['info']
            a = request.POST['author']
            reg = Todo(task=t,info=i,author=a)
            reg.save()
            fm = Task()
            visit = Todo.objects.filter(author=a)
            return render(request,'demo/show.html', {'v':visit})
    else:
        fm = Task()
    details = User.objects.get(pk=id)
    return render(request,'demo/add.html', {'form':fm, 'author':details.author}) 
        
# This function show all the items
def show(request,author):
    visit = Todo.objects.filter(author=author)
    return render(request,'demo/show.html', {'v':visit})

# This will edit or update the selected item
def update_data(request,id):
    if request.method == 'POST':
        obj = Todo.objects.get(pk=id)
        fm = Task(request.POST, instance=obj)
        if fm.is_valid():
            fm.save()
    else:
        obj = Todo.objects.get(pk=id)
        fm = Task(instance=obj)
    return render(request, 'demo/update.html',{'form':fm, 'obj':obj})


# This function will delete the item
def delete_data(request, id):
    if request.method == 'POST':
        obj = Todo.objects.get(pk=id)
        p = obj.author
        obj.delete()
        visit = Todo.objects.filter(author=p)
    return render(request,'demo/show.html',{'v':visit})