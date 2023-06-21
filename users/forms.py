from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.shortcuts import redirect
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

admin_group, created = Group.objects.get_or_create(name='Admins')
content_type = ContentType.objects.get_for_model(Group)
permission = Permission.objects.get(content_type=content_type, codename='view_group')
admin_group.permissions.add(permission)


admin_group, created = Group.objects.get_or_create(name='Author')
content_type = ContentType.objects.get_for_model(Group)
permission = Permission.objects.get(content_type=content_type, codename='view_group')
admin_group.permissions.add(permission)




class signUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())

    class Meta:
        model = User
        fields = {'username','email','password1','password2'}

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)


class AdminPanelMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            if not request.user.is_authenticated or not request.user.groups.filter(name='Admins').exists():
                return redirect('login')
        response = self.get_response(request)
        return response




