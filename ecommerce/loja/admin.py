from django.contrib import admin
from .models import *

admin.site.register(Categoria)
admin.site.register(Moeda)
admin.site.register(Produto)
admin.site.register(Compra)