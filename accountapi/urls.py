from django.urls import path
from accountapi.views import userloginView, userlogoutView, usersignupView, userdetailView, userlistView

urlpatterns = [
    path('signup/', usersignupView, name='user-signup'),
    path('login/', userloginView, name='user-login'),
    path('logout/', userlogoutView, name='user-logout'),
    path('userlist/', userlistView, name='user-list'),
    path('userdetail/<int:pk>/', userdetailView, name='user-detail')
]