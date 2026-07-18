from django.urls import path
from . import views

urlpatterns = [
    path('first_chars/', views.CharErha.as_view(), name='mcs'),
    path('first_info/', views.Info.as_view(), name='meee'),
    path('chars_list/', views.CharErhaView.as_view(), name='chars_list'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('chars_list/<int:id>/', views.CharDetailView.as_view(), name='chars_detail'),
]
