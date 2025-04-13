from django.contrib import admin
from .models import Group, User, Avatar


admin.site.register([Group, User, Avatar])

