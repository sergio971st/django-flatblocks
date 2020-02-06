from django.contrib import admin
from flatblocks.models import FlatBlock


def admin_register_flatblocks(filter_list=None):
    class FlatBlockAdmin(admin.ModelAdmin):
        ordering = ['slug', ]
        list_display = ('slug', 'header', 'subdomain', 'content', 'all_subdomains')
        if filter_list:
            list_filter = filter_list
        search_fields = ('slug', 'header', 'content', 'subdomain')

    admin.site.register(FlatBlock, FlatBlockAdmin)
