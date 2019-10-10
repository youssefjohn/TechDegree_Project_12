from .models import User_details, Project, User, PositionModel
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm, forms




class User_form(forms.ModelForm):
    class Meta:
        model=User
        fields = ('username', 'email', 'password')



class EditProfile_form(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields = ('username', 'email',)



class UserDetails_form(forms.ModelForm):
    class Meta:
        model= User_details
        fields= ('bio', 'picture')






class Project_form(forms.ModelForm):
    class Meta:
        model=Project
        fields=('title', 'description', 'project_timeline')


class Position_form(forms.ModelForm):
    class Meta:
        model= PositionModel
        fields='__all__'



class EditProject_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'related_skill', 'project_timeline')



class EditPosition_form(forms.ModelForm):
    class Meta:
        model = PositionModel
        fields = '__all__'



