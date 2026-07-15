from django.contrib import admin
from . import models

@admin.register(models.CharsErha)
class PersonMkAdmin(admin.ModelAdmin):
    exclude = ('views',)
    
admin.site.register(models.Fragments)