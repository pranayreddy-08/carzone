from django.contrib import admin
from .models import Car
from django.utils.html import format_html


def approve_cars(modeladmin, request, queryset):
    queryset.update(is_approved=True)
approve_cars.short_description = 'Approve selected cars'


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'car_title', 'owner', 'city', 'model', 'year', 'price', 'is_approved', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_approved', 'is_featured')
    list_filter = ('is_approved', 'city', 'model', 'body_style', 'fuel_type')
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type', 'owner__username')
    actions = [approve_cars]

admin.site.register(Car, CarAdmin)
