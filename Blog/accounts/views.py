from django.shortcuts import render

# Create your views here.
def post(request):
    return render(request, "index.html")

def home(request):
    return render(request, "homepage.html")
