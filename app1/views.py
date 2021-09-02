from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"a.html",{'link':'https://www.youtube.com/'})


def expression(request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+2*b
    return render(request,'output.html',{'result':c})
    # return render(request,'output.html')
