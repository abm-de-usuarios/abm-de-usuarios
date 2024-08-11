# from django.shortcuts import render, get_object_or_404, redirect
# # from ..models import Profile
# # from ..forms import profile_form

# def profile_detail(request, id):
#     profile = get_object_or_404(Profile, id=id)
#     return render(request, 'profile_detail.html', {'profile': profile})

# # Agregar vista para actualizar un perfil existente
# def profile_update(request, id):
#     profile = get_object_or_404(Profile, id=id)
#     if request.method == 'POST':
#         form = profile_form(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile-detail', id=id)
#     else:
#         form = profile_form(instance=profile)
#     return render(request, 'profile_form.html', {'form': form, 'profile': profile})
