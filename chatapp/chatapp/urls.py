from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from room import urls as room_urls
from core.views import frontpage, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("admin/", admin.site.urls),
    path('rooms/', include(room_urls))
]
