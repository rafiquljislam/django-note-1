from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.utils.html import format_html


class Categories(models.Model):
    categories = models.CharField(max_length=200)
    def __str__(self):
        return self.categories
    class Meta:
        db_table = 'Categories' # database name
        verbose_name='Catagory' #Admin page name
        verbose_name_plural ='Catagorys' #Admin page plural name




class Posts(models.Model):
    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    ]
    title = models.CharField(max_length=150)
    img = models.ImageField(upload_to='postimg/')
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    categorie = models.ManyToManyField(Categories, related_name='categaties')
    date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='d')

    # def __str__(self):
    #     return self.title
    def thumbnail(self):
        return format_html('<img width="70" src="/media/%s" />' % self.img)
    thumbnail.short_description = "Post Thumbnail"
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']

class PostsForm(forms.ModelForm):
    """Form definition for Posts."""
    class Meta:
        """Meta definition for Posts."""
        model = Posts
        fields = '__all__'
        widgets={
            'categorie':forms.CheckboxSelectMultiple(attrs={'class':'form-contorl','placeholder':'Title'})
        }
