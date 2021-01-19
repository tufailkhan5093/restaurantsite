from django.shortcuts import render

# Create your views here.
def home(request):
    context={'home':'active'}
    return render(request,'home.html',context)
def timing(request):
    context={'timing':'active'}
    return render(request,'timing.html',context)

def aboutus(request):
    context={'aboutus':'active'}
    return render(request,'aboutus.html',context)
def contactus(request):
    context={'contactus':'active'}
    return render(request,'contact.html',context)

def pricing(request):
    context={'pricing':'active'}
    return render(request,'pricing.html',context)
