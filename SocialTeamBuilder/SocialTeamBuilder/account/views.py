from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import User_form, UserDetails_form, EditProfile_form
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required



def index_view(request):
    return render(request, 'index.html')



def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        form = {'username':username,'email':email, 'password':password}
        new_form = User_form(data=form)





        if new_form.is_valid():
            new_form = new_form.save(commit=False)
            new_form.set_password(new_form.password)
            user = new_form.save()


            form2 = UserDetails_form()
            form2 = form2.save(commit=False)
            form2.bio = ''
            form2.picture = None
            form2.relation = user
            details = form2.save()


            return HttpResponseRedirect(reverse('index'))
        else:
            print('not valid')


    return render(request, 'account/signup.html')


def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        person = authenticate(username = username, password = password)

        if person:
            if person.is_active:
                login(request, person)
                return HttpResponseRedirect(reverse('index'))

        else:
            print('no user found')

    return render(request, 'account/signin.html')


@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required()
def profile_view(request):
    person = request.user
    return render(request, 'account/profile.html', {'person':person})



@login_required()
def profile_edit_view(request):
    if request.method == 'POST':
        form1 = EditProfile_form(instance=request.user, data=request.POST)
        if form1.is_valid():
            form1.save()
            update_session_auth_hash(request, user=request.user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print('form not valid')

    else:
        form1 = EditProfile_form()
        print("not post.")

    person = request.user
    return render(request, 'account/profile_edit.html', {'person':person})








