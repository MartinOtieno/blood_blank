from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('about', views.about_page, name='about_page'),
    path('blood', views.blood_page, name='blood_page'),
]
