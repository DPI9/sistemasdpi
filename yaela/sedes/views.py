# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Sede, Campo
from .forms import SedeForm, CampoForm

def sede_list(request):
    sedes = Sede.objects.all()
    return render(request, 'sedes/sede_list.html', {'sedes': sedes})

def sede_create(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sede_list')
    else:
        form = SedeForm()
    return render(request, 'sedes/sede_form.html', {'form': form})

def sede_update(request, idsede):
    sede = get_object_or_404(Sede, idsede=idsede)
    if request.method == 'POST':
        form = SedeForm(request.POST, instance=sede)
        if form.is_valid():
            form.save()
            return redirect('sede_list')
    else:
        form = SedeForm(instance=sede)
    return render(request, 'sedes/sede_form.html', {'form': form})

def sede_delete(request, idsede):
    sede = get_object_or_404(Sede, idsede=idsede)
    if request.method == 'POST':
        sede.delete()
        return redirect('sede_list')
    return render(request, 'sedes/sede_confirm_delete.html', {'sede': sede})
