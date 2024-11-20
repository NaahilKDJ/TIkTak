from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.utils import timezone
from .forms import CustomUserCreationForm
from .models import Post
from posts.models import Post

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

class HomeView(TemplateView):
    template_name = 'home.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profil.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_posts'] = Post.objects.filter(user=self.request.user).order_by('-dateCreation')
        return context