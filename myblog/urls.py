from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='Home'),
    path('about/', views.about,name='About'),
    path('contact/', views.contact,name='Contact'),
    path('dashboard/', views.dashboard,name='Dashboard'),
    path('logout/', views.user_logout,name='Logout'),
    path('signup/', views.user_signup ,name='Signup'),
    path('login/', views.user_login,name='Login'),
    path('addpost/', views.add_post,name='Addpost'),
    path('editpost/<int:id>/', views.edit_post ,name='Editpost'),
    path('deletepost/<int:id>/', views.delete_post ,name='Deletepost'),
    

]