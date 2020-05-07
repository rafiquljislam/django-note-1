from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class PostsConfig(AppConfig):
    name = 'posts'


class MyAdminConfig(AdminConfig):
    default_site = 'posts.admin.MyAdminSite'
    verbose_name = "APRafiq Administration"