from django.shortcuts import render, get_object_or_404, redirect
from .models import Group
from .forms import GroupForm 
from django.db.models import Q

from django.contrib import messages


def group_list(request):
     # se obtiene el valor del imput
    search_query = request.GET.get("search", "")
    # se busca el rol sin importar que tengo mayuscula o minuscula
    groups = Group.objects.filter(Q(name__icontains=search_query))
    return render(request, 'group/group_list.html', {'groups': groups})

def group_detail(request, id):
    group = get_object_or_404(Group, id=id)
    return render(request, 'group/group_detail.html', {'group': group})

# Agregar vista para crear un nuevo grupo
def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'group/group_create.html', {'form': form})

# Agregar vista para actualizar un grupo existente
def group_update(request, id):
    group = get_object_or_404(Group, id=id)
    
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request,'Grupo actualizado')            
        else:
            messages.error(request,'Error al actualizar el grupo') 
        return render(request, 'group/group_edit.html', {'form': form, 'group': group})
    else:
        form = GroupForm(instance=group)
    return render(request, 'group/group_edit.html', {'form': form, 'group': group})

# Agregar vista para eliminar un grupo existente
def group_delete(request, id):
    group = get_object_or_404(Group, id=id)
    if request.method == 'POST':
        group.delete()
    return redirect('group_list')