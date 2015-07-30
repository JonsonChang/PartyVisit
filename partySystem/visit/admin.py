from django.contrib import admin

# Register your models here.
from .models import address
from .models import history
from .models import people

admin.site.register(address)
admin.site.register(history)
admin.site.register(people)

