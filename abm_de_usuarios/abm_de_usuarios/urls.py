
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('home/',views.home,name="home"),
    path("role/",include("role.urls")),
    path("group/",include("group.urls")),
    path("user/",include("user.urls")),
    # path("profile/",include("profile.urls")), #hay que definir como se va a mostar el perfil del usuario 
   
    
]
