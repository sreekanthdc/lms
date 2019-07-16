from django.urls import path
from . import views
urlpatterns = [
    path('', views.myIndex, name='myIndex'),
    path('checklogin/', views.checkLogin, name="checkLogin")
]
