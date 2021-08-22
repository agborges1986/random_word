from django.shortcuts import redirect, render, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    request.session["count"]=1
    request.session["word"]=get_random_string(length=14)
    return render(request,"indexrnd.html")

def random(request):
    request.session["word"]=get_random_string(length=14)
    request.session["count"]=request.session["count"]+1
    return redirect("/random_word/success/")

def clear(request):
    request.session["word"]=""
    request.session["count"]=0
    return redirect("/random_word/success/")

def success(request):
    return render(request,"indexrnd.html")