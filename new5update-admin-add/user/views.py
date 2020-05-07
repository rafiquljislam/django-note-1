from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin



class Register(View):
    def get(self,request):
        form = UserCreationForm()
        context={
            'form':form
        }
        return render(request,'register.html',context)
    def post(self,request):
        data=UserCreationForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('login')


class Login(View):
    def get(self,request):
        form = AuthenticationForm()
        context={
            'form':form
        }
        return render(request,'login.html',context)
    def post(self,request):
        user = AuthenticationForm(request.POST)
        if user is None:
            return redirect ('login')
        else:
            login(request,user)
            return redirect('home')

class Logout(View):
    def get(self,request):
        if(request.user.is_authenticated):
            logout(request)
            return redirect('login')

class Profile(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'profile.html')


