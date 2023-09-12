from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User


# Create your views here.
def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'SessionManager/base.html', param)
    else:
        return redirect('/SessionManager/login')



def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        # print(uname, pwd)
        if User.objects.filter(username=uname).count()>0:
            return HttpResponse('Username already exists.')
        else:
            user = User(username=uname, password=pwd)
            user.save()
            return redirect('/SessionManager/login')
    else:
        return render(request, 'SessionManager/signup.html')



def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('/SessionManager/home')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'SessionManager/login.html')


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('/SessionManager/login')
    return redirect('/SessionManager/login')