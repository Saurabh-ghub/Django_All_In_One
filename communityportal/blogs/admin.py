from django.contrib import admin
from .models import Posts

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']

