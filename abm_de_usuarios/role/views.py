from django.shortcuts import render, get_object_or_404, redirect
from .models import Role
from .forms import RoleForm
from django.db.models import Q
from django.contrib import messages


def role_list(request):
     # se obtiene el valor del imput
    search_query = request.GET.get("search", "")
    # se busca el rol sin importar que tengo mayuscula o minuscula
    roles = Role.objects.filter(Q(name__icontains=search_query))
    return render(request, 'role/role_list.html', {'roles': roles})

def role_detail(request, id):
    role = get_object_or_404(Role, id=id)
    return render(request, 'role/role_detail.html', {'role': role})

# Agregar vista para crear un nuevo rol
def role_create(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm()
    return render(request, 'role/role_create.html', {'form': form})



# Agregar vista para actualizar un rol existente
def role_update(request, id):
    role = get_object_or_404(Role, id=id)
    
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            messages.success(request,'Rol actualizado')            
        else:
            messages.error(request,'Error al actualizar el rol') 
        return render(request, 'role/role_edit.html', {'form': form, 'role': role})
    else:
        form = RoleForm(instance=role)
    return render(request, 'role/role_edit.html', {'form': form, 'role': role})




# Agregar vista para eliminar un rol existente
def role_delete(request, id):
    role = get_object_or_404(Role, id=id)
    if request.method == 'POST':
        role.delete()
        
    return redirect('role_list')
