from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm
from django.contrib import messages
from django.db.models import Q



def user_list(request):
     # se obtiene el valor del imput
    search_query = request.GET.get("search", "")
    # se busca el rol sin importar que tengo mayuscula o minuscula
    users = User.objects.filter(Q(username__icontains=search_query))
    return render(request, 'user/user_list.html', {'users': users})

def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'user/user_detail.html', {'user': user})

# Agregar vista para crear un nuevo usuario
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user/user_create.html', {'form': form})

# Agregar vista para actualizar un usuario existente
def user_update(request, id):
    user = get_object_or_404(User, id=id)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Usuario actualizado')            
        else:
            messages.error(request,'Error al actualizar el usuario') 
        return render(request, 'user/user_edit.html', {'form': form, 'user': user})
    else:
        form = UserForm(instance=user)
    return render(request, 'user/user_edit.html', {'form': form, 'user': user})

# Agregar vista para eliminar un usuario existente
def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
    return redirect('user_list')