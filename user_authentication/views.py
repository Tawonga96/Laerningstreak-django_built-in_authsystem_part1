from django.shortcuts import render, redirect
from .forms import UserAuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.


def UserAuthLogin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()

            login(request, user)
            username=form.cleaned_data['username']
            messages.success(request, 'Welcome ' + username)
            return redirect('dashboard')           
    else:
        form=AuthenticationForm()
    
    context={'form': form}
    return render(request, 'user_authentication/login.html', context)



def UserAuthRegistration(request):
    # check request method if it is Post 
    if request.method == 'POST':
        # Form initialisation and passing data from request
        form=UserAuthenticationForm(request.POST)
        # Form validation
        if form.is_valid():
            # Save the user to database
            form.save()
            # retrieve user name with cleaned data
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account created for : ' + user)
            return redirect('login')

    else:
        form=UserAuthenticationForm()

    context={'form': form}
    return render(request, 'user_authentication/register.html', context) 



def dashboard(request):
    return render(request,'user_authentication/dashboard.html')