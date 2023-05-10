from django.contrib import admin
from .models import Character, House, Place

# Register your models here.

admin.site.register(Character)
admin.site.register(House)
admin.site.register(Place)