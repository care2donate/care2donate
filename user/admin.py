
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

import nested_admin

from covid.models import CovidUserDetail
from user.models import Locality, User


class CovidUserDetailInline(nested_admin.NestedTabularInline):
    model = CovidUserDetail
    extra = 0


class UserResource(resources.ModelResource):
    class Meta:
        model = User


class UserAdmin(nested_admin.NestedModelAdmin, ImportExportModelAdmin):
    resource_class = UserResource
    inlines = [CovidUserDetailInline, ]
    list_display = ('name', 'gender', 'dob', 'locality', 'contact_number', )
    list_filter = ('gender', 'locality', )
    search_fields = ('id', 'name', 'contact_number')


admin.site.register(Locality)
admin.site.register(User, UserAdmin)
