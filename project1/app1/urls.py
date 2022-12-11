from django.urls import path
from . import views

urlpatterns = [
    path('av/', views.addOrder, name='add_url'),
    path('sv/', views.showOrder, name='show_url'),
    path('uv/<int:pk>/', views.updateOrder, name='update_url'),
    path('dv/<int:pk>/', views.deleteOrder, name = 'delete_url'),
]
