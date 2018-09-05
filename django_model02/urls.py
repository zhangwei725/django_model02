from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('login_view/', views.login_view),
    path('1/', views.insert),
    path('2/', views.bulk_create),
    path('3/', views.update),
    path('4/', views.ext),
]
