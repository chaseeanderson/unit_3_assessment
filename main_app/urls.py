from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='wishlist'),
  path('add/', views.ItemCreate.as_view(), name='add_item'),
]