from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .forms import LoginForm
from .forms import GestionProductosForm
from .models import Usuario
from .models import Comida



# Create your views here.
def index(request):
    return render(request, 'main/base.html', {})

def login(request):
    return render(request, 'main/login.html', {})

def signup(request):
    return render(request, 'main/signup.html', {})

def loggedin(request):
    return render(request, 'main/loggedin.html', {})


def loginReq(request):
    tipo = 0
    url = ''
    id = 0
    email = request.POST.get("email")
    password = request.POST.get("password")
    for p in Usuario.objects.raw('SELECT * FROM usuario'):
        if p.contraseña == password and p.email == email:
            tipo=p.tipo
            if (tipo==0):
                url= 'main/baseAdmin.html'
            elif (tipo == 1):
                url = 'main/baseAlumno.html'
            elif (tipo == 2):
                url = 'main/baseVFijo.html'
            elif (tipo == 3):
                url= 'main/baseVAmbulante.html'
        id = p.id
        tipo = p.tipo
    request.session['id'] = id
    request.session['tipo'] = tipo
    request.session['email'] = email
    return render(request, url, {"email" : email, "tipo" : tipo, "id": id})

def gestionproductos(request):
    return render(request, 'main/gestion-productos.html', {})

def vendedorprofilepage(request):
    return render(request, 'main/vendedor-profile-page.html', {})

def formView(request):
   if request.session.has_key('id'):
      email = request.session['email']
      tipo = request.session['tipo']
      id = request.session['id']
      if (tipo == 0):
          url = 'main/baseAdmin.html'
      elif (tipo == 1):
          url = 'main/baseAlumno.html'
      elif (tipo == 2):
          url = 'main/baseVFijo.html'
      elif (tipo == 3):
          url = 'main/baseVAmbulante.html'
      return render(request, url, {"email" : email, "tipo" : tipo, "id": id})
   else:
      return render(request, 'main/login.html', {})

def logout(request):
    try:
        del request.session['id']
    except:
       pass
    return render(request, 'main/base.html', {})

def register(request):
    tipo = request.POST.get("tipo")
    nombre = request.POST.get("nombre")
    email = request.POST.get("email")
    password = request.POST.get("password")
    horaInicial = request.POST.get("horaIni")
    horaFinal = request.POST.get("horaFin")
    formasDePago =[]
    if not (request.POST.get("formaDePago0") is None):
        formasDePago.append(request.POST.get("formaDePago0"))
    if not (request.POST.get("formaDePago1") is None):
        formasDePago.append(request.POST.get("formaDePago1"))
    if not (request.POST.get("formaDePago2") is None):
        formasDePago.append(request.POST.get("formaDePago2"))
    if not (request.POST.get("formaDePago3") is None):
        formasDePago.append(request.POST.get("formaDePago3"))
    usuarioNuevo = Usuario(nombre=nombre,email=email,tipo=tipo,contraseña=password,avatar="jpge",formasDePago=formasDePago,horarioIni=horaInicial,horarioFin=horaFinal)
    usuarioNuevo.save()
    return render(request, 'main/loggedin.html', {"email" : email})

def productoReq(request):
    if request.method == "POST":
        Formulario = GestionProductosForm(request.POST)
        if Formulario.is_valid():
            producto = Comida()
            producto.nombre = request.POST.get("nombre")
            producto.precio = request.POST.get("precio")
            producto.stock = request.POST.get("stock")
            producto.descripcion = request.POST.get("descripcion")
            producto.categorias = request.POST.get("categoria")
            producto.save()
        else:
            return render(request, 'main/gestion-productos.html', {"respuesta": "¡Ingrese todos los datos!"})
    return render(request, 'main/vendedor-profile-page.html', {})