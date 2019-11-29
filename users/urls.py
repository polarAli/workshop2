from django.urls import path

from .views import LoginView, SignupView, ProfileView, UsersListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('list/', UsersListView.as_view(), name='users-list'),
]