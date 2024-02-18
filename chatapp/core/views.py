from django.shortcuts import render
from .forms import SignUpForm, InputForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def frontpage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})
