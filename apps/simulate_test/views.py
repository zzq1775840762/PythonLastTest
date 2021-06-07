from django.shortcuts import render
from apps.simulate_test.models import User,Result
# Create your views here.

def index(request):
    results = Result.objects.filter(result=3).order_by('-score')
    return render(request, 'index.html', {'field':results})
