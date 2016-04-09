from django.contrib import admin
from nana.models import fecha,imagen,galeria,imagen_galeria_principal

class imagenAdmin(admin.ModelAdmin):
	model         = imagen
	list_display  = ('titulo','descripcion','imagen_g','logo','fecha')

class fechaAdmin(admin.ModelAdmin):
	model         = fecha
	list_display  = ('anio',)
class galeriaAdmin(admin.ModelAdmin):
	model 		    = galeria
	list_display  = ('pk','padre','img')
class imagen_galeria_principalAdmin(admin.ModelAdmin):
  model         = imagen_galeria_principal
  list_display  = ('pk','imagen_principal','Galeria')

admin.site.register(imagen,imagenAdmin)
admin.site.register(fecha,fechaAdmin)
admin.site.register(galeria,galeriaAdmin)
admin.site.register(imagen_galeria_principal,imagen_galeria_principalAdmin)

