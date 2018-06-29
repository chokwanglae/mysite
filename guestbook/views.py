from django.shortcuts import render
from django.http import HttpResponseRedirect
from guestbook.models import Guestbook

# Create your views here.

def deleteform(request):
    #uestbook = Guestbook()
    #guestbook.name = request.POST['name']
    #guestbook.password = request.POST['password']
    #guestbook.message = request.POST['message']
    count = Guestbook.objects.filter(id=request.POST['id']).filter(password='').count()

    if count != 0:
        Guestbook.objects.filter(id=request.POST['id']).filter(password='').delete()

    # guestbook.save()


def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')

    context = {'guestbook_list': guestbook_list}
    return render(request, 'guestbook/index.html',context)

def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')
