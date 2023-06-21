from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.core.mail import send_mail
from .forms import  signUpForm, ContactForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout
from .forms import ChangePasswordForm
from django.template.loader import render_to_string

# Create your views here.

def signup(request):
    form = signUpForm()
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('Home')
        else:
            print('Form is invalid')
    return render(request, 'signup.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            
            
            html_message = render_to_string('email_template.html', {'name':name,'email':email, 'message' :message})
            
            send_mail(
                'The contact form subject',
                'this is the message',
                'Noreply@Med.com',
                ['Noreply@Med.com'],
                html_message=html_message
            )
            return redirect('Home')
    else:
        form = ContactForm()
    return render(request, 'ContactUs.html', {'form': form})



def settings(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            if not user.check_password(form.cleaned_data['current_password']):
                form.add_error('current_password', 'Your current password is incorrect.')
            else:
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                update_session_auth_hash(request, user)
                logout(request)
                messages.success(request, 'Password changed successfully. You have been logged out.')
                return redirect('login')
    else:
        form = ChangePasswordForm()
    return render(request, 'settings.html', {'form': form})

