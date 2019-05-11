from django.shortcuts import render
from .models import Setting, Request
from django.http import JsonResponse

def home(request):
    return render(request,'homepage.html')

def GetNumMessages(request):
    if request.method == "GET":
        messages = Request.objects.all()
        count = str(messages.count())
        return JsonResponse(count, safe=False)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Request.objects.create(name=name,email=email,subject=subject,message=message)
    return render(request,'contact.html')