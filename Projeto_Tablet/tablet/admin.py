from django.contrib import admin
from .models import Pessoa, TokenUsuario


admin.site.register(Pessoa)
admin.site.register(TokenUsuario)
