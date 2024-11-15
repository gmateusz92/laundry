# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User

# class RegisterForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True, label='Imię')
#     last_name = forms.CharField(max_length=30, required=True, label='Nazwisko')

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

# class LoginForm(AuthenticationForm):
#     pass


from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# class RegisterForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True, label='Imię')
#     last_name = forms.CharField(max_length=30, required=True, label='Nazwisko')

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if User.objects.filter(username=username).exists():
#             raise ValidationError("Nazwa użytkownika jest już zajęta.")
#         return username

#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Hasła nie pasują do siebie.")
#         if len(password1) < 8:
#             raise ValidationError("Hasło musi mieć co najmniej 8 znaków.")
#         return password2

#     def clean_first_name(self):
#         first_name = self.cleaned_data.get('first_name')
#         if first_name:
#             return first_name.capitalize()
#         return first_name

#     def clean_last_name(self):
#         last_name = self.cleaned_data.get('last_name')
#         if last_name:
#             return last_name.capitalize()
#         return last_name


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="Imię")
    last_name = forms.CharField(max_length=30, required=True, label="Nazwisko")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Nazwa użytkownika jest już zajęta.")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Hasła nie pasują do siebie.")
        return password2

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if first_name:
            return first_name.capitalize()
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if last_name:
            return last_name.capitalize()
        return last_name


class LoginForm(AuthenticationForm):
    pass
