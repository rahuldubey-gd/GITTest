from django.shortcuts import render
# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def welcomepage(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')