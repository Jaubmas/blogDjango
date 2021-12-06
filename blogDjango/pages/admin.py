from re import search
from django.contrib import admin
from .models import Page
# Register your models here.

#adding more configurations
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('hidden',)
    list_display = ('title', 'hidden', 'created_at')

admin.site.register(Page, PageAdmin)

title = "Panel de gestión"
subtitle = "Administración"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle