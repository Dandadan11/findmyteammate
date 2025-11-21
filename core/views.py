from django.shortcuts import render
from .models import Profile

def home(request):
    profiles = Profile.objects.all().order_by('-created_at')  # Сортировка по дате
    return render(request, 'core/home.html', {'profiles': profiles})