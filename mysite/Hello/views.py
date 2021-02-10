from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Contact

# Create your views here.
def homep(request):
    return render(request,'index.html')

def reg(request):
    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name= name
        contact.email=email
        contact.subject=subject
        contact.save()
        # return HttpResponse("<h1>THANK FOR CONTACT US</h1>")
        result()


    return render(request,'form.html')

def result(request):
    return render(request,'result.html')


    
