from django.urls import path

from .views import user_home_view

urlpatterns = [
    path('home', user_home_view, name='home')
]
