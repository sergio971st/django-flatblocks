from django.contrib import admin
from django.conf import settings
from flatblocks.models import FlatBlock


class FlatBlockAdmin(admin.ModelAdmin):
    ordering = ['slug', ]
    list_display = ('slug', 'header', 'subdomain', 'content', 'all_subdomains')
    list_filter = ('all_subdomains',)
    search_fields = ('slug', 'header', 'content', 'subdomain')


if not settings.CANCAEL_ADMIN_AUTO_REGISTRATION:
    admin.site.register(FlatBlock, FlatBlockAdmin)
