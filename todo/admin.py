from django.contrib import admin
from .models import Todolist
# Register your models here.

class Admin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Todolist, Admin)
