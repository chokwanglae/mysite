from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def guestbook(request):
    return render(request, 'main/guestbook.html')

def add(request):
    return render(request, 'main/add.html')

def emaillist(request):
    return render(request, 'main/emaillist.html')

def deletform(request):
    return render(request, 'main/deleteform.html')