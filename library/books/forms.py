from django import forms

class BookForm(forms.Form):
    title=forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    language = forms.CharField(max_length=100)
    pages = forms.IntegerField()
    price = forms.IntegerField()
    image=forms.ImageField()
