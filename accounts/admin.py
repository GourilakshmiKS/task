from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Custom)
admin.site.register(Product)
admin.site.register(Order)
