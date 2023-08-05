
from django.urls import path

from Agence.views import index, suite_detail

urlpatterns = [
    path('', index, name="home"),
    
    #/Agence/<suite_id>/
    path('Agence/<int:suite_id>/', suite_detail, name='detail'),
]

