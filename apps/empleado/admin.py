from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import empleado


class EmpleadoInline(admin.StackedInline):
	model = empleado
	can_delete = False
	verbose_name_plural = 'empleado'

## Define a new User admin
class UserAdmin(UserAdmin):
	inlines = (EmpleadoInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(empleado)
