
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send_email', views.send_email, name='send_email'),
    path('success_view', views.success_view, name='success'),
]
