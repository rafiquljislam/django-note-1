from django.shortcuts import render, redirect
from  django.contrib.auth.forms import UserCreationForm, AuthenticationForm #login form
from django.views.generic.edit import FormView
from django.views.generic import View
from .forms import UserRegisterFrom, UserUpdateFrom, ProfileUpdateFrom
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



class Register(View):
    def get(self,request):
        context = {
            'form':UserRegisterFrom()
        }
        return render(request,'user/register.html',context)
    def post(self,request):
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}! You are now able to login. ')
            return redirect('login')
        else:
            messages.warning(request, 'Please Fill the form Correctly')
            return redirect('register')

class Profile(LoginRequiredMixin,View):
    def get(self,request):        
        context = {
            'u_form':UserUpdateFrom(instance=request.user),
            'p_form':ProfileUpdateFrom(instance=request.user.profile)
        }
        return render(request,'user/profile.html',context)
    def post(self,request):
        u_form=UserUpdateFrom(request.POST,instance=request.user)
        p_form=ProfileUpdateFrom(request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been Updated')
            return redirect('profile')
        else:
            messages.warning(request, 'Please Fill the form Correctly')
            return redirect('profile')