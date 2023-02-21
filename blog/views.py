import pdb
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

 
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model=Post


class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='post'
    ordering=['-date_posted']
    extra_context={'latest_posts': Post.objects.order_by('-date_posted')[:5]}
    paginate_by=4


class UserPostListview(ListView):
    model=Post
    context_object_name='post'
    template_name ='blog/user_post.html'
    paginate_by=4
    
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


def home(request):
    queryset=Post.objects.all(),
    
    data={
        'latest_posts':queryset.objects.earliest('date_posted')[:5],
        'post':queryset,
        'title':'home page'
    }
    
    return render(request,'blog/home.html',data)


def about(request):
    post={
        'title':'about page'
    }
    return render(request,'blog/about.html',post)