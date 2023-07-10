from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from sweetify import success,warning,error
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
            success(request,'Usuario registrado correctamente')
            return redirect('inicio')
        else:
            error(request,'Error al registrar usuario')
            form = add_invalid_class(form)
            context = {
                'form':form
            }
            return render(request,'pages/m_user/registrar.html',context)
    else:
        form = FormRegister()
    context = {
        'form':form
    }
    return render(request,'pages/m_user/registrar.html',context)

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
                success(request,'Bienvenido {}'.format(user.username))
                return redirect('inicio')
            else:
                warning(request,'Usuario o contraseña incorrectos')
        context = {
            'form':data_user
        }
        return render(request,'pages/m_user/entrar.html',context)
    else:
        context = {
            'form':FormLogin()
        }
        return render(request,'pages/m_user/entrar.html',context)

def salir(request):
    logout(request)
    success(request,'Sesión cerrada correctamente')
    return redirect('inicio')

def add_invalid_class(form):
    for field in form.errors:
        form[field].field.widget.attrs.update({'class': 'form-control is-invalid'})
    return form