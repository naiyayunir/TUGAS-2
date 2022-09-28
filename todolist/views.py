import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task

daftar_task = []
# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    data_todo = Task.objects.filter(user=request.user)
    context = {
        'todolist' : data_todo,
        'usermame' : user.username
    }
    return render(request, "todolist.html", context)

def register_pengguna(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = redirect('todolist:login')
    response.delete_cookie('last_login')
    return response

@login_required(login_url='login/')
def create_task(request):
    if request.method == 'POST':
        user = request.user
        date = str(datetime.date.today())
        title = request.POST.get('title')
        description = request.POST.get('description')
        if(len(daftar_task)==0):
            objek = Task(user.id,1,date,title,description)
        else:
            objek = Task(user.id,daftar_task[-1].id+1,date,title,description)
        daftar_task.append(objek)
        print(user.id)
        objek.save()
        messages.success(request, 'Task baru kamu udah berhasil ditambah!')
        return redirect('todolist:show_todolist')
    context = {}
    return render(request, 'create_task.html', context)

