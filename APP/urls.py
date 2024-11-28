from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name='home'),
    path("login/",login,name='login'),
    path("register/",register,name='register'),
    path('logout/', logout, name='logout'),
    path('delete/<int:project_id>/', delete_project, name='delete_project'),
    path('project/edit/', edit_project, name='edit_project'),
    path('project/add/', add_project, name='add_project'),
]