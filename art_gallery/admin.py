from django.contrib import admin
from .models import Location, Category, Image

# # Register your models here.
# class ImageAdmin(admin.ModelAdmin):
#     filter_horizontal =('tags',)


admin.site.register(Location)
admin.site.register(Image)
admin.site.register(Category)
