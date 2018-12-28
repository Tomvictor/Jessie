from django.contrib import admin
from core.models import *

# Register your models here.

admin.site.site_header = 'Jacinta Jose | ADMIN'
admin.site.site_title = 'Jacinta Jose'

admin.site.register(Posts)