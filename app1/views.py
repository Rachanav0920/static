from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to app1.index page....</h1>")

def demo1(request):
    return render(request,"demo1.html",{"name":"Rachana"})

def demo2(request,a,b):
    return render (request,"demo2.html",{'a':int(a),'b':int(b)})

def demo3(request):
    return render(request,"demo3.html",{'fruits':['apple','banana','orange','mango']})

#def demo4(request):
 #   det={'name':"Rachana","age":24,"Desig":"Associate Software Engineer"}
 #   return render(request,"demo3.html",{'fruits':['apple','banana','orange','mango'],'det':det})

def demo5(request):
    return render(request,"Sample2.html")   

def sample3(request):
    return render(request,"sample3.html")    