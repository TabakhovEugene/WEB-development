from django.contrib import admin
from .models import BugReport, FeatureRequest

# @admin.register(BugReport)
# class BugReportAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'status', 'created_at')
#     list_filter = ('status',)
#     search_fields = ('title', 'description')
#
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'description', 'status')
#         }),
#         ('Additional Information', {
#             'fields': ('created_at', 'updated_at'),
#             'classes': ('collapse',)
#         }),
#     )
#
# @admin.register(FeatureRequest)
# class FeatureRequestAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'priority', 'created_at')
#     list_filter = ('priority',)
#     search_fields = ('title', 'description')
#
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'description', 'priority')
#         }),
#         ('Additional Information', {
#             'fields': ('created_at', 'updated_at'),
#             'classes': ('collapse',)
#         }),
#     )

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Основная информация', {'fields': ('title', 'project', 'task', 'description', 'priority', 'status')}),
        ('Дополнительная информация', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('description',)

    actions = ['change_status']

    def change_status(self, request, queryset):
        queryset.update(status='closed')

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('priority', 'created_at')
    search_fields = ('title', 'description')

    fieldsets = (
        ('Основная информация', {'fields': ('title', 'project', 'task', 'description', 'priority', 'status')}),
        ('Дополнительная информация', {'fields': ('created_at', 'updated_at')}),
    )

    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('description',)

# admin.site.register(BugReport)
# admin.site.register(FeatureRequest)
