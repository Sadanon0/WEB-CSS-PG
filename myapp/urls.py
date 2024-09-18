from django.contrib import admin
from django.urls import path
from .views import index
from myapp import views

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('f1', views.f1),
    path('f2', views.f2),
    path('f3', views.f3),
    path('manager', views.manager),
]
