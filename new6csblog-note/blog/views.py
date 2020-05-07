from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import (
                                    View,
                                    TemplateView,
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

class Home(ListView):
    model = Post
    template_name = 'blog/index.html' # default = app/modle_viewtype.html
    context_object_name = 'posts' # default=object_list
    ordering = ['-id']

class PostDetilView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    # for only login admin can create post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # for only login admin user can edit her post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    # for only login admin user can Delete her post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
