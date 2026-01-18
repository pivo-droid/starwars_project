from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('character/1/', views.character1, name='character1'),
    path('character/2/', views.character2, name='character2'),
    path('character/3/', views.character3, name='character3'),
]
