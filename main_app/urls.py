from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.ItemCreate.as_view(), name='add_item'),
  path('delete/<int:item_id>/', views.delete_item, name='delete_item')
]