from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):

    list_filter = ( 'actors__last_name', )


class PersonAdmin(admin.ModelAdmin): pass


class CountryAdmin(admin.ModelAdmin): pass


admin.site.register(Movie,MovieAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(Country,CountryAdmin)

