from django.contrib import admin
from nana.models import fecha,imagen

class imagenAdmin(admin.ModelAdmin):
	model        = imagen
	list_display = ('titulo','descripcion','imagen_g','fecha')

class fechaAdmin(admin.ModelAdmin):
	model        = fecha
	list_display = ('anio',)


admin.site.register(imagen,imagenAdmin)
admin.site.register(fecha,fechaAdmin)

