from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blogViews
from user import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogViews.Home.as_view(), name='home'),
    path('post/new', blogViews.PostCreateView.as_view(), name='post'),
    path('post/<int:pk>/', blogViews.PostDetailView.as_view(), name='post_detale'),
    path('post/<int:pk>/update', blogViews.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delate', blogViews.PostDeleteView.as_view(), name='post_delate'),
    path('register/', userViews.Register.as_view(), name='register'),
    path('profile/', userViews.Profile.as_view(), name='profile'),
    path('login/', authViews.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
