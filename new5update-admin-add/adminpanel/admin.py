from django.contrib import admin
from posts.models import Post,Catagory
from django.utils.html import format_html

class MyAdminSite(admin.AdminSite):
    admin.AdminSite.site_header = "Welcome Admin"
    admin.AdminSite.site_title = "rafiq"
    admin.AdminSite.index_title = "AP rafiq Blog"

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','date','status','author','thumbnail')
    list_display_links = ('title',)
    list_filter = ('title',)
    list_select_related = False
    list_per_page = 20
    list_max_show_all = 50
    list_editable = ('status',)
    search_fields = ('id','title','date','status',)
    date_hierarchy = None
    save_as = False
    save_as_continue = True
    save_on_top = False
    preserve_filters = True
    inlines = []

    
    # Actions
    def change_status_p(self, request, queryset):
        queryset.update(status='p')
    change_status_p.short_description = 'Publish Selected Post'
    def change_status_d(self, request, queryset):
        queryset.update(status='u')
    change_status_d.short_description = 'Unpublish Selected Post'
    def change_status_w(self, request, queryset):
        queryset.update(status='w')
    change_status_w.short_description = 'wait Selected Post'    
    
    
    # Actions
    actions = ['change_status_p','change_status_d','change_status_w']
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True


class CatagoryAdmin(admin.ModelAdmin):    
    list_display = ('__str__',)
    list_display_links = ()
    list_filter = ('title',)
    list_select_related = False
    list_per_page = 20
    list_max_show_all = 50
    list_editable = ()
    search_fields = ('id','title','date',)
    date_hierarchy = None
    save_as = False
    save_as_continue = True
    save_on_top = False
    preserve_filters = True
    inlines = []


admin.site.register(Post,PostAdmin)
admin.site.register(Catagory,CatagoryAdmin)

# admin_site = MyAdminSite()
# admin_site.register(Post,PostAdmin)
# admin_site.register(Catagory,CatagoryAdmin)