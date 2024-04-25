from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('news/<str:category>/', views.get_news, name='news'),  # Страница с новостями по категориям
]
