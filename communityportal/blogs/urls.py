from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('/about/',views.about,name="about"),
     path('/contact/',views.contact,name="contact"),
     path('/user_login/',views.user_login,name="user_login"),
     path('/user_logout/',views.user_logout,name="user_logout"),
     path('/signup/',views.signup,name="signup"),
     path('/dashboard/',views.dashboard,name="dashboard"),
     path('/add_post/',views.add_post,name="add_post"),
     path('/update_post/<int:id>/',views.update_post,name="update_post"),
     path('/delete_post/<int:id>/',views.delete_post,name="delete_post"),
]
