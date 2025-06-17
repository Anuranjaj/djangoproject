from django.shortcuts import render

#Addition
from app1.forms import AdditionForm
def addition(request):
    if (request.method == "POST"):
        print(request.POST)
        return render(request, 'addition.html')

    form_instance=AdditionForm()
    return render(request, 'addition.html',{'form':form_instance})

def factorial(request):

    return render(request, 'factorial.html')

def bmi(request):
    return render(request, 'bmi.html')

from app1.forms import SignupForm
def signup(request):
    form_instance=SignupForm()
    return render(request,'signup.html',{'form':form_instance})
