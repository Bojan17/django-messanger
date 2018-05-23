from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='all'),
    path('create/', views.CreatePost.as_view(), name='create'),
    path('detail/<pk>', views.SinglePost.as_view(), name='single')
]
