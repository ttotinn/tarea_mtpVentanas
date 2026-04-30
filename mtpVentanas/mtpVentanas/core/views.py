from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada con éxito")
            return redirect('menu')
    else:
        form = UserCreationForm()
    return render(request, 'core/registro.html', {'form': form})

def menu(request):
    return render(request, 'core/menu.html')

def imagenes(request):
    return render(request, 'core/imagenes.html')

def informacion(request):
    return render(request, 'core/informacion.html')