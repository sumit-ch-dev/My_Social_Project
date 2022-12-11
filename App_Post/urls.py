from django.urls import path
from App_Post import views

app_name = 'App_Post'

urlpatterns = [
    path("", views.home, name='home'),
]
