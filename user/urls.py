from django.urls import path 
from .views import SignupView, CustomLoginView, HomeView, ProfileView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name='inscription'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
