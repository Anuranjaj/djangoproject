from django.shortcuts import render

#Addition
#from app1.forms import AdditionForm
def addition(request):
    #GET Request
    if(request.method=="POST"):
        print(request.POST)
        n1=request.POST['num1']
        n2= request.POST['num2']
        result=int(n1)+int(n2)
        context={'result':result}
        return render(request,'addition.html',context)
    #form_instance=AdditionForm() #empty form object
    return render(request, 'addition.html')

def factorial(request):
    if(request.method=="POST"):
        n=
    return render(request, 'factorial.html')

def bmi(request):
    return render(request, 'bmi.html')
def signup(request):
    return render(request,'signup.html')
