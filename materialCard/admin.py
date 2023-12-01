from django.contrib import admin
from .models import MaterialCard

class MaterialCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploadImage', 'description', 'anisotropic', 'materialType')

# Register your models here.

admin.site.register(MaterialCard, MaterialCardAdmin)