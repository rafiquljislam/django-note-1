
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import clsssview, show

urlpatterns = [
    path('', clsssview.as_view(), name="clsss" ),
    path('', show.as_view(), name="show" ),
]