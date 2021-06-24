from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.PostView.as_view(), name='post_list'),
    path('post/new/', views.post_new, name='new'),
    path('post/<int:pk>/edit/', views.post_edit, name='edit'),
    path('post/<int:pk>/edit/delete/', views.post_delete, name='delete'),
]