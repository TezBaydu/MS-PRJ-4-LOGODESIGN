from django.contrib import admin
from .models import Company, Project, Package


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'description',
        'logoimage',
    )

    ordering = ('name',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'company',
        'image',
    )

    ordering = ('sku',)


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'friendly_name',
        'price',
        'image',
        'logo_count_request',
        'quality_request',
        'support_request',
        'production_days',
    )

    ordering = ('sku',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Package, PackageAdmin)
