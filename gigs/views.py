from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions, filters
from .models import Gig
from .serializers import GigSerializer

class GigListCreateView(generics.ListCreateAPIView):
    queryset = Gig.objects.all()
    serializer_class = GigSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class GigDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GigSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Gig.objects.filter(created_by=self.request.user)
    
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Gig

@login_required
def provider_dashboard(request):
    gigs = Gig.objects.filter(posted_by=request.user)
    return render(request, 'provider_dashboard.html', {'gigs': gigs})

from django.shortcuts import get_object_or_404, redirect

@login_required
def seeker_dashboard(request):
    gigs = Gig.objects.all()
    favorites = request.user.favorite_gigs.all()
    return render(request, 'seeker_dashboard.html', {'gigs': gigs, 'favorites': favorites})

@login_required
def favorite_gig(request, gig_id):
    gig = get_object_or_404(Gig, id=gig_id)
    gig.favorited_by.add(request.user)
    return redirect('seeker_dashboard')
