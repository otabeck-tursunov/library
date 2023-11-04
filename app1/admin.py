from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

# admin.site.register(Muallif)
# admin.site.register(Student)
# admin.site.register(Kitob)
# admin.site.register(Record)

@admin.register(Muallif)
class MuallifAdmin(ModelAdmin):
    search_fields = ('ism', 'id'),

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    search_fields = ('ism', 'id')
    list_display = ('ism', 'jins', 'kitob_soni')
    list_display_links = ('ism',)
    list_editable = ('kitob_soni',)
    list_filter = ('jins',)
    list_per_page = 10


@admin.register(Kitob)
class KitobAdmin(ModelAdmin):
    search_fields = ('nom', 'muallif__ism', 'janr' )
    list_filter = ('janr', )

@admin.register(Record)
class RecordAdmin(ModelAdmin):
    search_fields = ('student__ism', 'kitob__nom')
    # autocomplete_fields = ('student',)
    list_filter = ('qaytardi',)

