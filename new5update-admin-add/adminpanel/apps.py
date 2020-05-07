from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig
class AdminpanelConfig(AppConfig):
    name = 'adminpanel'

class MyAdminConfig(AdminConfig):
    default_site = 'adminpanel.admin.MyAdminSite'
    verbose_name = "AP-Administration"