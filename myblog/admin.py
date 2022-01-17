from django.contrib import admin
from .models import Blogpost

# Register your models here.
@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display=['id','title','desc','autho']
