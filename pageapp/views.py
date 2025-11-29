from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import GlassLoginForm, GlassRegisterForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def login_register_view(request):
    # Definimos qué pestaña debe estar activa (por defecto login)
    active_tab = 'login'

    if request.method == 'POST':
        # Verificamos qué botón se presionó usando el 'name' del botón submit
        if 'action' in request.POST and request.POST['action'] == 'login':
            
            # --- LÓGICA DE LOGIN ---
            login_form = GlassLoginForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('login') # CAMBIA 'inicio' por el name de tu url home
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
                active_tab = 'login' # Mantenemos pestaña login si falla
                register_form = GlassRegisterForm() # Reiniciamos el otro form

        elif 'action' in request.POST and request.POST['action'] == 'register':
            
            # --- LÓGICA DE REGISTRO ---
            register_form = GlassRegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                # Guardamos nombre, apellido y email (UserCreationForm solo guarda user/pass por defecto)
                user.first_name = register_form.cleaned_data.get('first_name')
                user.last_name = register_form.cleaned_data.get('last_name')
                user.email = register_form.cleaned_data.get('email')
                user.save()
                
                login(request, user) # Logueamos automáticamente al registrar
                messages.success(request, f"¡Bienvenido, {user.username}!")
                return redirect('index')
            else:
                messages.error(request, "Error en el registro. Revisa los campos.")
                active_tab = 'register' # Cambiamos a pestaña registro si falla
                login_form = GlassLoginForm()
        
        else:
            # Fallback por si acaso
            login_form = GlassLoginForm()
            register_form = GlassRegisterForm()

    else:
        # Petición GET (primera vez que entra)
        login_form = GlassLoginForm()
        register_form = GlassRegisterForm()

    return render(request, 'login.html', {
        'login_form': login_form,
        'register_form': register_form,
        'active_tab': active_tab
    })

def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('login')