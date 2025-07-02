from django.urls import path
from .views import GigListCreateView, GigDetailView

urlpatterns = [
    path('gigs/', GigListCreateView.as_view(), name='gig-list-create'),
    path('gigs/<int:pk>/', GigDetailView.as_view(), name='gig-detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('provider/dashboard/', views.provider_dashboard, name='provider_dashboard'),
    # Add other paths below
]

path('seeker/dashboard/', views.seeker_dashboard, name='seeker_dashboard'),
path('gig/<int:gig_id>/favorite/', views.favorite_gig, name='favorite_gig'),
