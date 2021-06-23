from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='new'),
    path('post/<int:pk>/edit/', views.post_edit, name='edit'),
    path('post/<int:pk>/edit/delete/', views.post_delete, name='delete'),
    path('order_by_author/', views.post_list_author, name='post_by_author'),
    path('filter_by_published/', views.post_list_published, name='filter_by_published'),
]