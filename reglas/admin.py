from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib import admin
from reglas.models import Crons
from reglas.models import MultiSelectField
from reglas.models import MultiSelectFormField
# Re-register UserAdmin

admin.site.register(Crons)

