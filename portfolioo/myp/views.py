from django.shortcuts import render
from django.http import HttpResponse
from.models import*

# Create your views here.

# def index(request):
#     return render(request,'index.html')
def index(request):
    if request.method=="POST":
        name=request.POST.get('fname')
        eadres=request.POST.get('eads')
        mobile=request.POST.get('mnb')
        emailsub=request.POST.get('esub')
        yourmsg=request.POST.get('ym')
        
        ob=formdata(fname=name,eads=eadres,mnb=mobile,esub=emailsub,ym=yourmsg)
        ob.save()
        
        return render(request,'index.html')
    return render(request,'index.html')