from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    path('create/', views.createtodo, name='createtodo'),
    path('todo/<int:todo_pk>/', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete/', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete/', views.deletetodo, name='deletetodo'),

    path('current/', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
]

