# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from to_do.models import Todo

admin.site.register(Todo)