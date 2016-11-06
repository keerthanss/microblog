from django import forms

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
class EditProfileForm(forms.Form):
    profile_name = forms.CharField(label='Profile Name', max_length=100)   
    bio = forms.CharField(widget=forms.Textarea , label='bio')
