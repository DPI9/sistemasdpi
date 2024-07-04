from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.shortcuts import redirect

def saludo(request):
   return render(request, 'index.html', {
       'mensaje': 'Esto es un saludo de mi funcion'
       
   })
   
def panel(request):
   return render(request, 'user/panel.html', {
       'mensaje': 'Esto es un saludo de mi funcion'   
   })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        usuarios = authenticate(username=username, password=password)
        if usuarios:
            lg(request,usuarios)
            return redirect('panel')
            
    return render(request, 'users/login.html', {})

