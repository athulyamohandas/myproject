from django.shortcuts import render
from django.http import HttpResponse
from.models import *


# Create your views here.
# def index(request):
#     return render(request,'index.html')
def index(request):
    d = {
        'fields':pictures.objects.all()
    }

    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        ob = formdata(uname=name,em=email,sub=subject,mes=message)
        ob.save()
        return render (request,'index.html')
    return render(request,'index.html',d)







