from django.contrib import admin
from django.contrib.auth.models import User, Group
from clsss.models import Test
from .models import *
from django.utils.html import format_html

class MyAdminSite(admin.AdminSite):
    site_header = "Welcome Admin"
    site_title = "rafiq"
    index_title = "AP rafiq Blog"


class PostsAdmin(admin.ModelAdmin):

    """Encapsulate all admin options and functionality for a given model."""
    list_display = ('id','title',format_html('content'),'user','date','status','thumbnail')
    list_display_links = ('title',)
    list_filter = ('title',)
    list_select_related = False
    list_per_page = 20
    list_max_show_all = 100
    list_editable = ('status',)
    search_fields = ('title','content','id')

    def change_status_p(self, request, queryset):
        queryset.update(status='p')
    change_status_p.short_description = 'Publish Selected Post'
    

    def change_status_d(self, request, queryset):
        queryset.update(status='d')
    change_status_d.short_description = 'Draft Selected Post'
    

    def change_status_w(self, request, queryset):
        queryset.update(status='w')
    change_status_w.short_description = 'Withdrawn Selected Post'
    
    # Actions
    actions = ['change_status_p','change_status_d','change_status_w']
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True


# admin.site.register(Posts,PostsAdmin)
# admin.site.register(Categories)

admin_site = MyAdminSite()
admin_site.register(Posts, PostsAdmin)
admin_site.register(Categories)
admin_site.register([User,Group])
admin_site.register(Test)