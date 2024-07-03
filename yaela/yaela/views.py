from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
   return render(request, 'index.html', {
       'mensaje': 'Esto es un saludo de mi funcion'
       
   })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print (username)
        print (password)
    return render(request, 'users/login.html', {})