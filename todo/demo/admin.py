from django.contrib import admin
from .models import User,Todo

# Register your models here.

admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list = ('id','name','email','password')
    
admin.site.register(Todo)