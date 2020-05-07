from django.shortcuts import render,redirect
from .models import Categories, Posts, PostsForm



def home(request):
    context={
        'posts':Posts.objects.all()
    }
    return render(request,'index.html',context)


def posts(request):
    if request.method == 'POST':
        data = PostsForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            return redirect('home')
    context={
        'form':PostsForm()
    }
    return render(request,'post.html',context)


