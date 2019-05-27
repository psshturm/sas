from django.contrib import admin

# Register your models here.
from .models import Counterparties, SparkSettings, NotificationSettings, SourceSettings, News

class CounterpartiesAdmin(admin.ModelAdmin):
    list_display = ['name', "inn", "web_site", "risk", "с_time"]

class SparkSettingsAdmin(admin.ModelAdmin):
    list_display = ['cron_key']

class NotificationSettingsAdmin(admin.ModelAdmin):
    list_display = ['email']

class SourceSettingsAdmin(admin.ModelAdmin):
    list_display = ['url']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['news']


admin.site.register(Counterparties, CounterpartiesAdmin)
admin.site.register(SparkSettings, SparkSettingsAdmin)
admin.site.register(NotificationSettings, NotificationSettingsAdmin)
admin.site.register(SourceSettings, SourceSettingsAdmin)
admin.site.register(News, NewsAdmin)