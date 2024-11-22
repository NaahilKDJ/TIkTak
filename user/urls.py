from django.urls import path 
from .views import SignupView, CustomLoginView, HomeView, ProfileView, UserSearchView, UserDetailView, follow_user, like_post
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name='inscription'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/follow/', follow_user, name='follow-user'),
    path('post/<int:post_id>/like/', like_post, name='like-post'),
    path('delete-account/', delete_account, name='delete-account'),
]
