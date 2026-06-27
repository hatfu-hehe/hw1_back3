from django.urls import path
from . import views

urlpatterns = [
    path('first_chars/', views.char_erha, name='mcs'),
    path('first_info/', views.info, name='meee'),
]
