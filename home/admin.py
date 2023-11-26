from django.contrib import admin
from .models import rents, User, comments

# Register your models here.
admin.site.register(rents)
admin.site.register(User)
admin.site.register(comments)