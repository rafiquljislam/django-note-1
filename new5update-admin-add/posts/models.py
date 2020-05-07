from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.utils.html import format_html
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField
from django.db.models.signals import pre_save, post_save


class Catagory(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Post(models.Model):
    status = [
        ('u','Unpublish'),
        ('w','wait'),
        ('p','Publish'),
    ]
    title = models.CharField(max_length=200)
    content = HTMLField()
    img = models.ImageField(upload_to='img/')
    date = models.DateTimeField(auto_now_add=True)
    catagory = models.ManyToManyField(Catagory, default=None)
    status = models.CharField(max_length=1, choices=status, default='u')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    class Meta:
        db_table = 'postdetales'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']
    def thumbnail(self):
        return format_html('<img width="70" src="/media/%s" />' % self.img)

class PostForm(forms.ModelForm):
    """Form definition for Post."""
    class Meta:
        """Meta definition for Postform."""
        model = Post
        fields = '__all__'
        widgets= {
            'catagory':forms.CheckboxSelectMultiple(attrs={'class':'form-contorl'}),
            'content':TinyMCE(attrs={'class':'form-contorl'}),
        }


def befoe_catagory_save(sender, instance, **Kwargs):
    print('Creating Category For {} '.format(instance))

    

def after_catagory_save(sender, instance, **Kwargs):
    print('Save Category For {} '.format(instance))

pre_save.connect(befoe_catagory_save, sender=Catagory)

post_save.connect(after_catagory_save, sender=Catagory)