# ✨ Django Glassmorphism Base + Auth System

![Estado](https://img.shields.io/badge/Estado-Activo-success?style=flat-square)
![Django](https://img.shields.io/badge/Django-5.x-092E20?style=flat-square&logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-purple?style=flat-square&logo=bootstrap)

Una base de proyecto moderna y elegante que combina la potencia de **Django** con una interfaz visual **Glassmorphism** (efecto vidrio). 

Este repositorio incluye un sistema de autenticación completo (Login, Registro y Logout) totalmente integrado con el diseño, utilizando formularios personalizados de Django y estilos CSS avanzados.

---

## 📸 Vistazo Rápido

| Pantalla de Inicio (Logeado) | Login / Registro (Tabs) |
|:---:|:---:|
| <img width="1871" height="917" alt="image" src="https://github.com/user-attachments/assets/082541ce-8f34-444f-b8df-84299a16e013" />
| <img width="1870" height="918" alt="image" src="https://github.com/user-attachments/assets/0be01703-a62c-4e8e-b09d-4ad685e9fc71" />
|
| *Menú desplegable de usuario y contenido dinámico.* | *Alternancia suave entre Login y Registro sin recargar.* |

---

## 🎨 Características Principales

### 💎 Frontend (UI/UX)
* **Glassmorphism UI:** Paneles traslúcidos, inputs de vidrio y desenfoque (`backdrop-filter`).
* **Fondo Animado:** Gradiente CSS dinámico que cambia suavemente.
* **Diseño Responsivo:** Bootstrap 5.3.3 adaptado a móviles.
* **Feedback Visual:** Alertas de vidrio para mensajes de éxito/error.

### ⚙️ Backend (Django)
* **Auth System Integrado:** Lógica completa para iniciar sesión, registrarse y cerrar sesión.
* **Formularios Personalizados (`forms.py`):** Mixin personalizado `GlassStyleMixin` que inyecta estilos CSS a los widgets de Django automáticamente.
* **Vistas Dinámicas:** El `navbar` cambia según el estado del usuario (muestra botón de "Acceder" o "Menú de Usuario").
* **Validaciones:** Manejo de errores nativo de Django visualizado con estilo.

---

## 🚀 Instalación y Puesta en Marcha

Sigue estos pasos para correr el proyecto en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/TESBrunoBRM/baseejemplo.git 
cd baseejemplo
```
2. Crear entorno virtual (Recomendado)
```Bash
python -m venv venv
```
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
3. Instalar dependencias
```Bash
pip install django
```
4. Migraciones de Base de Datos
Necesario para que funcione el sistema de usuarios de Django.
```Bash
python manage.py makemigrations
python manage.py migrate
```
5. Correr el servidor
```Bash
python manage.py runserver
```
Visita http://127.0.0.1:8000/ en tu navegador.

📂 Estructura del Proyecto
Plaintext
```bash
baseejemplo/
├── pageapp/
│   ├── templates/
│   │   ├── base.html       # Plantilla madre (Navbar, Footer, CSS)
│   │   ├── index.html      # Home dinámico (User Dropdown)
│   │   └── login.html      # Sistema de pestañas Login/Registro
│   ├── forms.py            # Lógica de estilos "Glass" para inputs
│   ├── views.py            # Controladores de Auth
│   └── urls.py             # Rutas (/, /login, /logout)
├── manage.py
└── db.sqlite3
```

📄 Licencia
Este proyecto es de código abierto. ¡Siéntete libre de usarlo para tus propios proyectos, tareas o prototipos!

<p align="center"> Hecho con ❤️ y Python por <a href="https://www.google.com/search?q=https://github.com/TESBrunoBRM">TESBrunoBRM</a> </p>
