from .models import User_details, Project, User
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













