from django.shortcuts import render,redirect

from books.forms import BookForm
from django.template.defaultfilters import title
from django.templatetags.i18n import language

from books.models import Book
def home(request):
    return render(request,'home.html')
def addbook(request):
    if (request.method == "POST"):
        t = request.POST['t']
        a = request.POST['a']
        l = request.POST['l']
        p = request.POST['p']
        pa = request.POST['pa']
        b = Book.objects.create(title=t, author=a,language=l,price=p,pages=pa)
        b.save()
        return render(request, 'addbook.html')
    return render(request,'addbook.html')

from books.forms import BookForm
def addbook1(request):
    if(request.method=="POST"):
        print(request.POST)
        form_instance=BookForm(request.POST)
        if form_instance.is_valid():
            #data = form_instance.cleaned_data
            b=Book.objects.create(title=form_instance.cleaned_data['title'],
                                  author=form_instance.cleaned_data['author'],
                                  language=form_instance.cleaned_data['language'],
                                  price=form_instance.cleaned_data['price'],
                                  pages=form_instance.cleaned_data['pages'])

            b.save()
        return redirect('books:viewbook')
    if(request.method=="GET"):
        form_instance=BookForm()
        return render(request,'addbook1.html',{'form':form_instance})
def viewbook(request):
    return render(request,'viewbook.html')