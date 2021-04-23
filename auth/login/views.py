from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users



@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('indexPage')
        else:
            messages.info(request, "Username or Password is Incorrect")

    return render(request, 'login.html')


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customers')
            user.groups.add(group)

            messages.success(request, "Account is created for " + username)
            return redirect('loginPage')

    context ={
        'form': form
    }

    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'customers'])
def indexPage(request):
    return render(request, 'index.html')

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def DashBoard(request):
    return render(request, 'dashboard.html')