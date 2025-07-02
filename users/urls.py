from django.urls import path
from .views import RegisterView, LoginView, DeleteView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('delete/', DeleteView.as_view()),
    path('logout/', LogoutView.as_view()),
]
