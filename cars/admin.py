from django.contrib import admin
from .models import Car
from django.utils.html import format_html


def approve_cars(modeladmin, request, queryset):
    queryset.update(is_approved=True)
approve_cars.short_description = 'Approve selected cars'


def reject_cars(modeladmin, request, queryset):
    queryset.update(is_approved=False)
reject_cars.short_description = 'Reject / unapprove selected cars'


class PendingApprovalFilter(admin.SimpleListFilter):
    title = 'Approval Status'
    parameter_name = 'approval'

    def lookups(self, request, model_admin):
        return [
            ('pending', 'Pending Approval'),
            ('approved', 'Approved'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'pending':
            return queryset.filter(is_approved=False)
        if self.value() == 'approved':
            return queryset.filter(is_approved=True)
        return queryset


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        if obj.car_photo:
            return format_html('<img src="{}" width="40" style="border-radius:50%;" />', obj.car_photo.url)
        return '-'
    thumbnail.short_description = 'Photo'

    def approval_status(self, obj):
        if obj.is_approved:
            return format_html('<span style="color:green; font-weight:bold;">&#10003; Approved</span>')
        return format_html('<span style="color:red; font-weight:bold;">&#9679; Pending</span>')
    approval_status.short_description = 'Status'

    def owner_name(self, obj):
        return obj.owner.username if obj.owner else 'Admin'
    owner_name.short_description = 'Submitted By'

    list_display = ('id', 'thumbnail', 'car_title', 'owner_name', 'city', 'model', 'year', 'price', 'approval_status', 'is_approved', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_approved', 'is_featured')
    list_filter = (PendingApprovalFilter, 'city', 'model', 'body_style', 'fuel_type')
    search_fields = ('car_title', 'city', 'model', 'owner__username')
    actions = [approve_cars, reject_cars]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('owner')


admin.site.register(Car, CarAdmin)
