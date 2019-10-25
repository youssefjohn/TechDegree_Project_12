from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('test/', views.test_view, name='test'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('other_persons_profile/<int:pk>', views.other_persons_profile, name='otherprofile'),
    path('profileedit/', views.profile_edit_view, name='profileedit'),
    path('project/<int:pk>', views.project_view, name='project'),
    path('project_new/', views.new_project_view, name='newproject'),
    path('project_edit/<int:pk>', views.edit_project_view, name='editproject'),
    path('project_delete/<int:pk>', views.delete_project_view, name='delete'),
    path('applications/', views.application_view, name='applications'),
    path('applications2/<int:pk>', views.application_view2_allows_filtering_of_projects, name='applications2'),
    path('apply/<int:pk>', views.apply_view, name='apply'),
    path('returnreject/<int:pk>', views.applications_returned_reject_view, name='returnreject'),
    path('returnaccept/<int:pk>', views.applications_returned_accept_view, name='returnaccept'),
    path('accept/', views.accepted_applications, name='accept'),
    path('reject/', views.rejected_applications, name='reject'),

]

