from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.utils import timezone
from .forms import CustomUserCreationForm
from posts.models import Post
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import UserFollow


# Create your views here.
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'inscription.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.dateCreationCompte = timezone.now()
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

class HomeView(TemplateView):
    template_name = 'home.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profil.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_posts'] = Post.objects.filter(user=self.request.user).order_by('-dateCreation')
        return context

class UserSearchView(ListView):
    model = get_user_model()
    template_name = 'user/search_results.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return self.model.objects.filter(
                Q(email__icontains=query) |
                Q(prenom__icontains=query) |
                Q(nom__icontains=query)
            ).exclude(email=self.request.user.email)
        return self.model.objects.none()

class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user/user_detail.html'
    context_object_name = 'profile_user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_user = self.get_object()
        context.update({
            'user_posts': Post.objects.filter(user=profile_user).order_by('-dateCreation'),
            'is_following': UserFollow.objects.filter(follower=self.request.user, following=profile_user).exists(),
            'followers_count': profile_user.followers.count(),
            'following_count': profile_user.following.count()
        })
        return context

@login_required
def follow_user(request, pk):
    user_to_follow = get_user_model().objects.get(pk=pk)
    if request.user != user_to_follow:
        if request.method == 'POST':
            if 'follow' in request.POST:
                UserFollow.objects.get_or_create(follower=request.user, following=user_to_follow)
            elif 'unfollow' in request.POST:
                UserFollow.objects.filter(follower=request.user, following=user_to_follow).delete()
    return redirect('user-detail', pk=pk)