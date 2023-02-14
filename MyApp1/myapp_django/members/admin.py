from django.contrib import admin
from .models import Member, User

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)
    prepopulated_fields = {"slug": ("firstname", "lastname")}

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Login", {'fields': ['id','username', 'password']}),
        ('Datos Personales', {'fields': ['firstname', 'lastname']}),
        ('Datos de Contacto', {'fields': ['email', 'address', 'phone']}),
    ]

admin.site.register(Member, MemberAdmin)
admin.site.register(User,UserAdmin)

# Register your models here.
