from django.db import models
from django import forms

class Test(models.Model):
    title = models.CharField(max_length=150)
    content  = models.TextField()
    def __str__(self):
        return self.title
    
class TestForm(forms.ModelForm):
    """Form definition for Test."""
    class Meta:
        """Meta definition for Testform."""
        model = Test
        fields = '__all__'

