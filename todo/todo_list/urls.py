from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.addItem, name='add'),
    path('delete/<item_id>', views.deleteItem, name='delete'),

]