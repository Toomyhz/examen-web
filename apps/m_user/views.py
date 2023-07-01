from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = FormRegister(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('home')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
    else:
        form = FormRegister()
    context = {
        'form':form
    }
    return render(request,'m_user/register.html',context)

def entrar(request):
    if request.method == 'POST':
        data_user = FormLogin(data=request.POST)
        is_valid = data_user.is_valid()
        if is_valid:
            user = authenticate(
                username=data_user.cleaned_data['username'],
                password=data_user.cleaned_data['password']
            )
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                data_user.add_error(None,'Usuario o contraseña incorrecta')
        context = {
            'form':data_user
        }
        return render(request,'m_user/login.html',context)
    else:
        context = {
            'form':FormLogin()
        }
        return render(request,'m_user/login.html',context)

def salir(request):
    logout(request)
    return redirect('home')