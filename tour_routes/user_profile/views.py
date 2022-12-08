from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.validators import validate_email

User = get_user_model()

@csrf_protect
def register(request):
    # susirenkame kintamuosius iš savo formos
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # Tikimės, kad klaidų nėra ir kintamąjam priskytiame reikšmę False, t.y. klaidos nėra
        error = False
        # darom tikrinimą username simbolių skaičių. Jei simbolių <5, išmes klaidą
        if not username or len(username) < 4 or User.objects.filter(username=username).first():
            messages.error(request, 'User not entered or user name already exists or user name less then 5 simbols.')
            error = True
        if not email or User.objects.filter(email=email).first():
            messages.error(request, 'Email not entered or user with this e-mail already exists.')
            error = True
        else:
            try:
                validate_email(email)
            except:
                messages.error(request, 'Invalid email.')
                error = True
        if not password or not password2 or password != password2:
            messages.error(request, "Password not entered, or not match.")
            error = True
        if not error:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'User registration successful. You can log in now.')
            return redirect('login')    
    return render(request, 'user_profile/register.html')

