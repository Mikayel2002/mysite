from django.urls import path
from blog import views

urlpatterns = [
    path('', views.create_article, name="home"),
]