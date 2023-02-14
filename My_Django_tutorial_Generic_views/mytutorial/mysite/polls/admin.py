from django.contrib import admin

from .models import Choice, Question, User,Anton


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Login", {'fields': ['username', 'password']}),
        ('Datos Personales', {'fields': ['firstname', 'lastname']}),
        ('Datos de Contacto', {'fields': ['email', 'address', 'phone']}),
    ]

# prueba para ver funcionamiento 
class AntonAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Anton1',{'fields':['field_1', 'field_2']}),
        ('Anton2',{'fields': ['field_3']}),
        ('Anton3',{'fields': ['field_4']})
    ]

admin.site.register(User, UserAdmin) # ver tabla user 
admin.site.register(Question, QuestionAdmin) # ver tabal question
admin.site.register(Anton,AntonAdmin)