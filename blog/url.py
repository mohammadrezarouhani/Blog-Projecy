from django.urls import path
from django.views.generic.edit import UpdateView
from .views import PostCreateView, PostListView,PostDetailView,PostUpdateView,PostDeleteView,UserPostListview
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('/user/post/<str:username>',UserPostListview.as_view(),name='user-post'),
    path('about/',views.about,name='blog-about'),
]
