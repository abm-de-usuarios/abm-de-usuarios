from django.urls import path
from . import views

urlpatterns = [
    
    # URLs para Role
    path('roles/', views.role_list, name='role_list'),
    path('roles/<int:id>/', views.role_detail, name='role_detail'),
    path('roles/create/', views.role_create, name='role_create'),
    path('roles/update/<int:id>', views.role_update, name='role_update'),
    path('roles/delete/<int:id>', views.role_delete, name='role_delete'),



]
