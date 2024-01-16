from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.LoginView, name='login_url'),
    path('register/', views.registerView, name='register_url'),
    path('login1/', views.user_login, name="login"),
    path('register1/', views.register, name='register'),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),




    path('', views.index, name="post_page"),
    path('create/', views.post_create, name="post_create"),
    path('blog/<int:id>/', views.post_detail, name="post_detail"),
    path('about/', views.about, name="about"),
    path('edit/', views.post_list, name='post_list'),
    path('update/<int:id>/', views.post_update, name='post_update'),
    path('delete/<int:id>/', views.post_delete, name='post_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)