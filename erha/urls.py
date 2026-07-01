from django.urls import path
from . import views

urlpatterns = [
    path('first_chars/', views.char_erha, name='mcs'),
    path('first_info/', views.info, name='meee'),
    path('chars_list/', views.char_erha_view, name='chars_list'),
    path('chars_list/<int:id>/', views.char_detail_view, name='chars_details'),
]
