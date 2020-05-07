from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from blog import views as blogViews
from user import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogViews.Home.as_view(), name='home'),
    path('register/', userViews.Register.as_view(), name='register'),
    path('login/', authViews.LoginView.as_view(template_name = 'user/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
    path('profile/', userViews.Profile.as_view(), name='profile'),
    path('post/<int:pk>/', blogViews.PostDetilView.as_view(), name='post_detail'),
    path('post/new/', blogViews.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', blogViews.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', blogViews.PostDeleteView.as_view(), name='post_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)