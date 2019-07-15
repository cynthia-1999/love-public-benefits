

# Register your models here.
from django.contrib import admin
from .import models

admin.site.register(models.Userinfo)

admin.site.register(models.ActVolum)

admin.site.register(models.ActInteg)

admin.site.register(models.ActJoin)

admin.site.register(models.ComJoin)


