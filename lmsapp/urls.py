from django.urls import path
from . import views
urlpatterns = [
    path('', views.myIndex, name='myIndex'),
    path('admin_lgn',views.admin_lgn, name='admin_lgn')
]
