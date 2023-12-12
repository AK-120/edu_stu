from django.shortcuts import render

# Create your views here.
def login(requests):
    return render(requests,'login.html')
