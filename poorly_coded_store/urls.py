from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_order', views.create_order),
    path('checkout/<int:order_id>', views.checkout)
]
