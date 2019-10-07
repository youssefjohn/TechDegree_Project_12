from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [

    path('test/', views.test_view, name='test'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profileedit/', views.profile_edit_view, name='profileedit'),
    path('project/', views.project_view, name='project'),
    path('project_new/', views.new_project_view, name='newproject'),
    path('project_edit/', views.edit_project_view, name='editproject'),



]

