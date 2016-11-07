from django import forms
from django.forms import Textarea
from models import User
from dal import autocomplete
class LogInForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Username', 'required' : True}),
                                    max_length=30)
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Password', 'required' : True}),
                                    max_length=30)
class RegisterForm(forms.Form):
    r_email = forms.EmailField(label="Email",
                                widget = forms.EmailInput(attrs={'placeholder':'Email', 'required' : True}),
                                max_length=30)
    r_username = forms.CharField( label="Username",
                                widget = forms.TextInput(attrs={'placeholder':'Username', 'required' : True}),
                                    max_length=30)
    r_password = forms.CharField( label="Password",
                                widget = forms.PasswordInput(attrs={'placeholder':'Password', 'required' : True}),
                                    max_length=30)

class PostForm(forms.Form):
    post_content = forms.CharField(widget = Textarea(attrs={
                                                        'rows': 3,
                                                        'class':'form-control',
                                                        'placeholder':'Start a Rypple..'
                                                    }),
                                    max_length = 256)
    public_privacy = forms.BooleanField(widget = forms.CheckboxInput(attrs={'checked':'checked'}),
                                        required=False)

class EditProfileForm(forms.Form):
    profile_name = forms.CharField(label='Profile Name', max_length=100)
    bio = forms.CharField(widget=forms.Textarea , label='bio')

class SearchForm(forms.Form):
    searchField = forms.CharField(label='search',
                    widget=forms.TextInput(attrs={'placeholder': 'Search'}))
