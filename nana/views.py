from django.template.response import TemplateResponse
from nana.models import imagen, fecha
def index(request):
	obj 	= get_all_img()
	return TemplateResponse(request,'index.html',obj)

def get_all_img():
	imagenes = []
	obj = imagen.objects.all()
	return {'lista':obj}
