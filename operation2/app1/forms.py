
from django import forms
from django.forms import PasswordInput


class AdditionForm(forms.Form):
    number1=forms.IntegerField()
    number2=forms.IntegerField()

class SignupForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=15,widget=PasswordInput)
    email=forms.EmailField()
    gender_choices=[('male',"Male"),('female',"Female")]
    gender = forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    role_choices=[('admin',"Admin"),('student',"Student")]
    role=forms.ChoiceField(choices=role_choices)

