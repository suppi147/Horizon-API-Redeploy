from django.urls import path
from . import views
app_name = "SessionManager"
urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('get_session_info/', views.get_session_info, name='get_session_info'),
    path('get_endpoints/', views.get_endpoints, name='get_endpoints'),
    path('get_instances/', views.get_instances, name='get_instances'),
]