# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Data
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('pollution','created_on','latitude','longitude')

admin.site.register(Data,DataAdmin)
