from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from .forms import ProfileForm

from .models import Profile, User
# Create your views here.

def register(request):
    """Register a new user. """
    if request.method != 'POST':
        # Display blank registration form. 
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

# can find profile url, but query needs to be fixed.
# can not find the user.
# userid = 1 and 2 invalid but 3 works. 
# can only work admin created users.
# deafult registraitons will be placed to auth_user, 
# but profile/id searchs in users_user.
def user_profile(request, user_id):
    """Show user Profile"""
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, id=user_id)
    context = {"user" : user, "profile": profile}
    return render(request, "profile/profile.html", context)


# def create_profile(request):
#     if request.method != 'POST':
#         # Display blank registration form. 
#         form = ProfileForm()
#     else:
#         # Process completed form.
#         form = ProfileForm(data=request.POST)

#         if form.is_valid():
#             form.save()
#             # Log the user in and then redirect to home page.
#             return redirect('learning_logs:index')

#     # Display a blank or invalid form.
#     context = {'form': form}
#     return render(request, 'profile/create.html', context)