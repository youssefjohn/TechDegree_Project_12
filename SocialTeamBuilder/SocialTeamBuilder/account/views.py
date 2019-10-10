from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from .forms import User_form, UserDetails_form, EditProfile_form, Position_form, Project_form, EditProject_form, EditPosition_form
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from .models import User_details, UserSkills, PositionModel, Project
from django.forms import modelformset_factory


def index_view(request):
    user = request.user
    projects = Project.objects.exclude(user=user)








    return render(request, 'index.html', {'projects':projects})



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
    projects = Project.objects.filter(user=person)
    projects2 = Project.objects.select_related().filter(user=person)
    return render(request, 'account/profile.html', {'person':person, 'projects':projects, 'projects2':projects2})



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


@login_required()
def project_view(request, pk):
    user = request.user

    project = get_object_or_404(Project, pk=pk)
    position = project.position.all()

    return render(request, 'account/project.html', {'project':project, 'position':position})


@login_required()
def new_project_view(request):
    user = request.user

    if request.method == 'POST':
        ptitle = request.POST.get('ptitle')
        pdescription = request.POST.get('pdescription')
        title = request.POST.get('title')
        description = request.POST.get('description')
        time = request.POST.get('Time')
        skill = request.POST.get('Skill')

        form = {'title':ptitle, 'description': pdescription}
        form2 = {'title':title, 'description': description, 'project_timeline':time}

        positionform = Position_form(data=form)
        projectform = Project_form(data=form2)

        if positionform.is_valid() and projectform.is_valid():
            positionform = positionform.save()
            projectform = projectform.save(commit=False)
            projectform.user = user
            projectform.save()
            projectform.position.add(positionform)
            try:
                a = UserSkills.objects.get(title=skill)
            except UserSkills.DoesNotExist:
                print('doesnt exist')
            else:
                projectform.related_skill.add(a)

            return HttpResponseRedirect(reverse('index'))

    else:
        positionform = Position_form()
        projectform = Project_form()

    return render(request, 'account/project_new.html')




@login_required()
def edit_project_view(request,pk):
    project = get_object_or_404(Project, pk=pk)
    position = project.position.all().first()


    if request.method == 'POST':
        print('post request')
        print(position)
        title = request.POST.get('title')
        description = request.POST.get('description')
        ptitle = request.POST.get('ptitle')
        pdescription = request.POST.get('pdescription')
        time = request.POST.get('time')
        skill = request.POST.get('skill')
        print(title, description, ptitle, pdescription, time, skill)

        items_for_project_form = {'title':title,'description':description, 'project_timeline':time}
        form1 = Project_form(instance=project, data=items_for_project_form)

        items_for_position_form = {'title':ptitle, 'description':pdescription}
        form2 = Position_form(instance=position, data=items_for_position_form)

        if form1.is_valid() and form2:
            form1.save()
            form2.save()
            try:
                a = UserSkills.objects.get(title=skill)
            except UserSkills.DoesNotExist:
                print('doesnt exist')
            else:
                project.related_skill.add(a)



            return HttpResponseRedirect(reverse('index'))

    return render(request, 'account/project_edit.html', {'project': project})




@login_required()
def delete_project_view(request, pk):

    delete = get_object_or_404(Project, pk=pk)

    delete.delete()

    return HttpResponseRedirect(reverse('account:profile'))



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












