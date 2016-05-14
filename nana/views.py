from django.template.response import TemplateResponse
from nana.models import imagen, fecha, galeria,imagen_galeria_principal,equipo as equipos
from importlib import import_module

def index(request):
  obj   = get_all_img()
  return TemplateResponse(request,'index.html',obj)

def get_all_img():
  obj = fecha.objects.all()
  return {'lista':obj}

def gal(request,img):
  imgs = galeria.objects.filter(padre=img)
  index_g = imagen_galeria_principal.objects.filter(Galeria=img)
  return TemplateResponse(request,'galeria.html',{'imagenes':imgs,'index_g':index_g})


def pagina(request,pagina=None,base=None):
  params=globals()[pagina]()
  return TemplateResponse(request,pagina+'.html',params)

def equipo(request):
  equip = equipos.objects.all()
  return TemplateResponse(request,'contacto.html',{'equipo':equip})

def contacto(request):
  algo ='lakjsdhflkajshflkajshdflkajsdh'
  return TemplateResponse(request,'contacto.html',{'imagenes':algo})