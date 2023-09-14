from pickle import FALSE
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
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


def checkLoginKeystone(uname,pwd):
    url = "http://127.0.0.1:5000/v3/auth/tokens"
    payload_getID = {
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": uname,
                        "domain": {
                            "name": "Default"
                        },
                        "password": pwd
                    }
                }
            }
        }
    }
    
    response_getID = requests.post(url, json=payload_getID)
    if response_getID.status_code == 201:
        # Successful response (HTTP status code 201)
        print("Authentication successful!")
        # You can access the authentication token in the response headers or body, depending on the API's structure.
        # For example, if the token is in the response body as JSON, you can access it like this:
        user_id = response_getID.json().get("token", {}).get("user", {}).get("id")
        print(f"user id: {user_id}")
        payload_getToken = {    
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "id": user_id,
                        "password": pwd
                    }
                }
            },
                "scope": {
                "project": {
                    "id": "ad4728f8d4f64678b37319afba7fb85c"
                }
            }
        }
    }
        response_getToken= requests.post(url, json=payload_getToken)
        if response_getToken.status_code == 201:
            print("Token successfully retreived!")
            headers_getToken = response_getToken.headers
            X_subject_token= headers_getToken.get('X-Subject-Token')
            print(f"X-subject-token: {X_subject_token}")
            return True
        else:
            # Handle authentication failure or other errors
            print(f"Authentication failed. Status code: {response_getToken.status_code}")
            print(f"Response content: {response_getToken.text}")
            return False
    else:
        # Handle authentication failure or other errors
        print(f"Authentication failed. Status code: {response_getID.status_code}")
        print(f"Response content: {response_getID.text}")
        return False

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        
        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user and checkLoginKeystone(uname,pwd):
            request.session['user'] = uname
            #return redirect('/SessionManager/home')
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