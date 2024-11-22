from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from user.models import UserFollow

# Create your views here.

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts-list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        # Get all posts except the current user's posts, ordered by date
        return Post.objects.exclude(user=self.request.user).order_by('-dateCreation')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

@login_required
def user_feed(request):
    # Get the list of users the current user is following
    following_users = UserFollow.objects.filter(follower=request.user).values_list('following', flat=True)
    # Fetch posts from the following users
    posts = Post.objects.filter(user__in=following_users).order_by('-dateCreation')
    return render(request, 'posts/feed.html', {'posts': posts})
