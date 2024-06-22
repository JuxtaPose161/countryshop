from django.shortcuts import render

from .form import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'users/register_complete.html')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
