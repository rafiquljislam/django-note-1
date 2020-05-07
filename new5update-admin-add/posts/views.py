from django.shortcuts import render,redirect
from .models import Post, PostForm
from django.views.generic import View,ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




class Home(TemplateView):
    template_name = 'index.html'
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'object_list':Post.objects.all()
        }
        return context
    

class Posts(LoginRequiredMixin,FormView):
    template_name = 'posts.html'
    form_class = PostForm
    success_url = ('/')

class Add(CreateView):
    model = Post
    fields = '__all__'
    # form_class = PostForm
    # template_name = 'posts/post_form.html'
    success_url = ('/')

class Edit(UpdateView):
    # model = Post
    # fields = '__all__'
    form_class = PostForm
    success_url = ('/')
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Post.objects.filter(pk=pk)

class Delete(DeleteView):
    model = Post
    success_url =reverse_lazy('home')