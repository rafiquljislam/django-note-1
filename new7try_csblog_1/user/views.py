from django.shortcuts import render, redirect
from .forms import UserReigstationForm, UserUpdateFrom, ProfileUpdateFrom
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView,
    View
)

class Register(View):
    def get(self,request):
        context={
            'form':UserReigstationForm()
        }
        return render(request,'user/register.html',context)
    def post(self,request):
        data = UserReigstationForm(request.POST)
        if data.is_valid():
            username = data.cleaned_data.get('username')
            data.save()
            messages.success(request, f"Your account created for {username} ! Now You can Login...!")
            return redirect('login')
        else:
            messages.warning(request, "Fill the form correctly..!!")
            return redirect('register')


class Profile(LoginRequiredMixin,View):
    def get(self,request):
        context={
            'u_form':UserUpdateFrom(instance=request.user),
            'p_form':ProfileUpdateFrom(instance=request.user.profile),
        }
        return render(request, 'user/profile.html', context)
    def post(self,request):
        u_form=UserUpdateFrom(request.POST, instance=request.user,)
        p_form=ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile, )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile is edite Success fully !")
            return redirect('profile')