from django.contrib import admin
from nana.models import fecha,imagen,galeria

class imagenAdmin(admin.ModelAdmin):
	model        = imagen
	list_display = ('titulo','descripcion','imagen_g','logo','fecha')

class fechaAdmin(admin.ModelAdmin):
	model        = fecha
	list_display = ('anio',)
class galeriaAdmin(admin.ModelAdmin):
	model 		 = galeria
	list_display = ('pk','padre','img')
admin.site.register(imagen,imagenAdmin)
admin.site.register(fecha,fechaAdmin)
admin.site.register(galeria,galeriaAdmin)

