from django.contrib import admin
from django.utils.html import format_html
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent', 'ordering', 'actions')
    list_editable = ('url', 'parent', 'ordering')

    def actions(self, obj):
        return format_html(
            '<a class="button" href="{}">View</a>',
            obj.url,
        )
    actions.short_description = 'Actions'


admin.site.register(MenuItem, MenuItemAdmin)
