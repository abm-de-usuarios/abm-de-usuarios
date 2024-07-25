# from django.shortcuts import render, get_object_or_404, redirect
# from ..models import User
# from ..forms import UserForm

# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'user_list.html', {'users': users})

# def user_detail(request, id):
#     user = get_object_or_404(User, id=id)
#     return render(request, 'user_detail.html', {'user': user})

# # Agregar vista para crear un nuevo usuario
# def user_create(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('user-list')
#     else:
#         form = UserForm()
#     return render(request, 'user_form.html', {'form': form})

# # Agregar vista para actualizar un usuario existente
# def user_update(request, id):
#     user = get_object_or_404(User, id=id)
#     if request.method == 'POST':
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('user-detail', id=id)
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'user_form.html', {'form': form, 'user': user})

# # Agregar vista para eliminar un usuario existente
# def user_delete(request, id):
#     user = get_object_or_404(User, id=id)
#     if request.method == 'POST':
#         user.delete()
#         return redirect('user-list')
#     return render(request, 'user_confirm_delete.html', {'user': user})
