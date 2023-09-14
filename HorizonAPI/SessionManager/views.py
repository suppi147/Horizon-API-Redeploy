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

def get_session_info(request):
    # Lấy session ID
    session_id = request.session.session_key
    # Lấy dữ liệu của session
    request.session['keystone'] = 'gAAAAABk7vPV1DIm86IOsex2HFvyfbuvX13PIdxrOPgYWr8GneWtZOTQDpNPqch6hchYBz1bzE2ewW9ZENPq8V0yQSmd2ZoEuDjrfCXb7XkHLusxat52s4jyeJTK21dVFDZebsXuwrFEdVYh936lQA_I--tilPUa4kJ7rkCnmSro9y3HEsnCrGM'
    x=request.session['keystone']
    session_data = request.session
    # Hiển thị thông tin session
    response = f'Session ID: {session_id}<br>'
    response += f'Session Data:{session_data}<br>'
    response += f'Session Openstack:{x}<br>'
    # Lặp qua dữ liệu của session và hiển thị từng cặp key-value
    for key, value in session_data.items():
        response += f'{key}: {value}<br>'

    return HttpResponse(response)