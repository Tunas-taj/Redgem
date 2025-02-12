from django.contrib import admin
from .models import register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('note', 'date')
    readonly_fields = ('date',)

# Registra el modelo con la configuración del admin
admin.site.register(register, RegisterAdmin)
