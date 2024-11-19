from django.urls import path
from .views import 
from .views import LoginView, SignupView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user/<int:pk>', Profil.as_view(), name='user-view'),
    # path('create/', .as_view(), name='facture-create'),
    # path('update/<int:pk>/', .as_view(), name='facture-update'),
    # path('delete/<int:pk>/', .as_view(), name='facture-delete'),
    path('login', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name='signup'),
]
