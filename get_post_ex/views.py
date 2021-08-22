from django.shortcuts import redirect, render, HttpResponse
from django.http.response import JsonResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def forms(request):
    return HttpResponse('Página de la aplicación para mostrar formulario')

def info(request):
    return HttpResponse('Página de la aplicación para la info')

def create_users(request):
    print ("Información del POST.....\n")
    print (request.POST)
    context={
        'name':request.POST['name'],
        'email':request.POST['email']
    }
    request.session["context"]=context
    return redirect("/success")

def success(request):
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    return render(request,"info.html",request.session["context"])