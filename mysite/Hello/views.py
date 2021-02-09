from django.shortcuts import render, HttpResponse
from django.template import loader
from Hello.models import Feedback
from .form import PostForm

# Create your views here.
def firstfunc(request):
    return render(request,'index.html')

def DetailView(request):
    form_class = PostForm()
    if request.method == "POST":
        form_class = PostForm(request.POST)
        if form_class.is_valid():
            objs = form_class.save()
        else:
            print("ERROR FORM INVALID")
    
