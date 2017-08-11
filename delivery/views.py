from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # if not request.user.is_authenticated:
    #     return render(request, 'unauthorized.html')
    return render(request, 'delivery/index.html')