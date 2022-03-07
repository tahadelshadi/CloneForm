from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.user.is_authenticated:
        redirect_url = '/'
        return redirect(redirect_url)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = '/'
            return redirect(redirect_url)
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است.",
                           extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, 'account/login.html')

@login_required
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    return render(request, 'account/login.html')