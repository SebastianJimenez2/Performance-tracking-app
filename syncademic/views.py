from django.http import HttpResponse
from django.shortcuts import render


# Create your api here.
def index(request):
    return render(
        request,
        'index.html',
        {
            'title': 'Syncademic',
            'message': 'Welcome to!',
        }
    )
