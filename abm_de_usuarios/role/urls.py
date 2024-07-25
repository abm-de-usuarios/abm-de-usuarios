from django.urls import path
from .views import index_views,role_views

urlpatterns = [
    path('',index_views.index, name='index_index'),
    
    # URLs para Role
  
    path('roles/', role_views.role_list, name='role_list'),
    path('roles/<int:id>/', role_views.role_detail, name='role_detail'),
    path('roles/create/', role_views.role_create, name='role_create'),
    path('roles/update/<int:id>', role_views.role_update, name='role_update'),
    path('roles/delete/<int:id>', role_views.role_delete, name='role_delete'),

    # # URLs para Group
    # path('groups/', group_views.group_list, name='group_list'),
    # path('groups/<int:id>/', group_views.group_detail, name='group_detail'),
    # path('groups/create/', group_views.group_create, name='group_create'),
    # path('groups/<int:id>/update/', group_views.group_update, name='group_update'),
    # path('groups/<int:id>/delete/', group_views.group_delete, name='group_delete'),
    

    # # URLs para User
    # path('users/', user_views.user_list, name='user_list'),
    # path('users/<int:id>/', user_views.user_detail, name='user_detail'),
    # path('users/create/', user_views.user_create, name='user_create'),
    # path('users/<int:id>/update/', user_views.user_update, name='user_update'),
    # path('users/<int:id>/delete/', user_views.user_delete, name='user_delete'),

    # # URLs para Profile
    # path('profile/<int:id>/', profile_views.profile_detail, name='profile_detail'),
    # path('profile/<int:id>/update/', profile_views.profile_update, name='profile_update'),
]
