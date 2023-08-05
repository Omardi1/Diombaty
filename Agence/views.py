from django.shortcuts import render, get_object_or_404
from .models import Suite

# Create your views here.
def index(request):
    all_suites = Suite.objects.all()
    return render(request, 'Agence/index.html', {'all_suites': all_suites})


def suite_detail(request, suite_id):
    suite = get_object_or_404(Suite, pk=suite_id)
    return render(request, 'Agence/detail.html', {'suite': suite})


    
    