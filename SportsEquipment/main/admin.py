from django.contrib import admin
from .models import ItemRequest, StudentBorrow, UserSites
# Register your models here.

admin.site.register(ItemRequest)
admin.site.register(StudentBorrow)
admin.site.register(UserSites)
