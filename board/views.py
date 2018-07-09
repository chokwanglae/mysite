from django.http import HttpResponseRedirect
from django.shortcuts import render


from board.models import Board

# Create your views here.
from user.models import User


def board(request):
    posts_list = Board.objects.all().order_by('-title')
    posts_list = {'posts_list': posts_list}
    return render(request, 'board/list.html',posts_list)

def writeform(request):
     #인증 체크
     authuser = request.session.get('authuser')
     if authuser is None:
         return HttpResponseRedirect('/user/loginform')

     return render(request, 'board/write.html')



def write(request):
    board = Board()
    user_id = request.POST.get('user_id')
    board.title = request.POST['title']
    board.content = request.POST['content']

    board.user = (User.objects.filter(id=request.session.get('authuser')['id']).filter(password=request.session.get('authuser')['password']))[0]

    board.save()
    return HttpResponseRedirect('/board')

def deleteform(request):

    id = request.GET.get('id')
    context = {'id': id}
    return render(request, 'board/',context)

def delete(request):
    # count = board.objects.filter(id=request.POST['id']).filter(password=request.POST['password']).count()
    #
    # if count != 0:
    #     Board.objects.filter(id=request.POST['id']).filter(password=request.POST['password']).delete()
    # # Guestbook.save()
    # return HttpResponseRedirect('/board')

    Board.objects.filter(id=request.GET['id']).filter(user_id=request.session['authuser'].get('id')).delete()
    return HttpResponseRedirect('/board')


def list(request):
    board = Board()
    user_id = request.POST.get('user_id')
    board.tilte = request.POST['title']
    board.content = request.POST['content']


    return render(request, 'board/list.html')
def view(request):
    board = Board.objects.filter(id=request.GET['id'])
    print(board)
    posts_list = {'posts_list': board}
    return render(request, 'board/view.html',posts_list)

def modifyform(request):
    posts_list = Board.objects.filter(id=request.GET['id'])

    print(board)

    posts_list = {'posts_list': posts_list}

    return render(request, 'board/modify.html', posts_list)


def modify(request):
    print(Board.objects.filter(id=request.POST['id']))
    posts= Board.objects.filter(id=request.POST['id'])
    print(posts)

    user_id = request.session['authuser']['id']


    posts.title = request.POST['title']

    posts.content = request.POST['content']

    posts.user =User.objects.get(id=user_id)
    posts.save()
    return render(request, 'board/veiw?id='+request['posts_id'])
