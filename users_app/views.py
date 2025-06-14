from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView,LogoutView


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created {username}')
            return redirect('login-page')
    else :
        form = UserRegisterForm()
    return render(request,'users_app/register.html',context={'form':form})

    
@login_required
def profile(request):

    if request.method == 'POST' :
         user_update_form = UserUpdateForm(request.POST,instance=request.user)
         profile_update_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

         if user_update_form.is_valid() and profile_update_form.is_valid():
             user_update_form.save()
             profile_update_form.save()
             messages.success(request, f'account has been updated!!')
             return redirect('profile-page')

    else :
         user_update_form = UserUpdateForm(instance=request.user)
         profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':user_update_form,
        'p_form':profile_update_form,
    }

    return render(request,'users_app/profile.html',context)




class Login(LoginView):
    template_name = 'users_app/login.html'



class Logout(LogoutView):
    template_name = 'users_app/logout.html'



