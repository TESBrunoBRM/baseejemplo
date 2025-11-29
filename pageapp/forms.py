from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

# --- Estilos comunes para tus inputs de vidrio ---
class GlassStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Aquí inyectamos tu clase CSS 'glass-input' y 'form-control'
            field.widget.attrs.update({
                'class': 'form-control glass-input',
                'placeholder': field.label  # Para que funcione el floating label
            })

# --- Formulario de Login Personalizado ---
class GlassLoginForm(GlassStyleMixin, AuthenticationForm):
    # El mixin se encarga de los estilos
    pass

# --- Formulario de Registro Personalizado ---
class GlassRegisterForm(GlassStyleMixin, UserCreationForm):
    # Añadimos campos extra si quieres (ej: nombre y apellido)
    first_name = forms.CharField(label="Nombre", max_length=30)
    last_name = forms.CharField(label="Apellido", max_length=30)
    email = forms.EmailField(label="Correo Electrónico")

    class Meta(UserCreationForm.Meta):
        model = User
        # Orden en que aparecen los campos
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')