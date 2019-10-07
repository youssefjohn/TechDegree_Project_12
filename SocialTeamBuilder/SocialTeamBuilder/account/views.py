from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import User_form, UserDetails_form, EditProfile_form, Position_form
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from .models import User_details, UserSkills, PositionModel
from django.forms import modelformset_factory


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

            a = User_details(relation=new_form)
            a = a.save()

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




# ******************************************
# ********** PROFILE ***********************
# ******************************************


@login_required()
def profile_view(request):
    person = request.user
    return render(request, 'account/profile.html', {'person':person})



@login_required()
def profile_edit_view(request):

    user = request.user

    if request.method == 'POST':
        form1 = EditProfile_form(instance=user, data=request.POST)
        form2 = UserDetails_form(instance=user.user_details, data=request.POST)



        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2 = form2.save(commit=False)

            if 'picture' in request.FILES:
                form2.picture = request.FILES['picture']
                print(form2.picture)
                form2.save()

                skill = request.POST.get('skill')
                print(skill)

                try:
                    a = UserSkills.objects.get(title=skill)
                except UserSkills.DoesNotExist:
                    print('doesnt exist')
                else:
                    user.user_details.skills.add(a)
            else:

                skill = request.POST.get('skill')
                print(skill)

                try:
                    a = UserSkills.objects.get(title=skill)
                except UserSkills.DoesNotExist:
                    print('doesnt exist')
                else:
                    user.user_details.skills.add(a)

            form2.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect(reverse('index'))


    return render(request, 'account/profile_edit.html', {'person':user})








# ******************************************
# ********** PROJECT ***********************
# ******************************************



def project_view(request):



    return render(request, 'account/project.html')



def new_project_view(request):
    print('view running')

    if request.method == 'POST':
        print("info posted")

        ptitle = request.POST.get('ptitle')
        pdescription = request.POST.get('pdescription')

        form = {'title':ptitle, 'description': pdescription}


        positionform = Position_form(data=form)

        if positionform.is_valid():
            print('form valid')
            positionform = positionform.save()
            return HttpResponseRedirect(reverse('index'))

        else:
            print('form not valid')


    else:
        positionform = Position_form()
        print('not POST')


    return render(request, 'account/project_new.html')





def edit_project_view(request):
    pass









# TRYING OUT FORMSETS
def test_view(request):
    Test = modelformset_factory(PositionModel, fields=('title', 'description'), extra=4)




    if request.method == 'POST':
        print(request.POST)

        form = Test(request.POST)
        form = form.save()


        print(request.POST)
        return HttpResponseRedirect(reverse('index'))

    form = Test()

    return render(request, 'account/test.html', {'formset':form})












