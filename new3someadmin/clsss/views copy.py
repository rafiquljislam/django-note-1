from django.shortcuts import render
from django.views.generic import ListView,View
from .models import Test

# class clsssview(ListView):
#     model= Test
#     template_name='clsss.html'

class clsssview(View):
    template_name='clsss.html'
    def get(self, request):
        data =Test.objects.all()
        return render(request, self.template_name, {'object_list':data})
