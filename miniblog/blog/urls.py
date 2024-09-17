from django.urls import path, include
from blog import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.user_login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.user_signup,name='signup'),
    path('addpost/',views.addpost,name='addpost'),
    path('updatepost/<int:id>',views.updatepost,name='updatepost'),
    path('deletepost/<int:id>',views.deletepost,name='deletepost'),
]