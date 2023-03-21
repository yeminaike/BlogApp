from django.urls import path
from . import views

urlpatterns = [
    path('greet/', views.greet, name='greet'),
    path('game/', views.game, name='game'),
    path('hello/', views.hello, name='hello'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('', views.PostListView.as_view(), name="home"),
    path('new/', views.PostCreateView.as_view(), name='post_new'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name="post_delete"),
    path('<int:pk>/edit', views.PostUpdateView.as_view(), name="post_edit")


]


