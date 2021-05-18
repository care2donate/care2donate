
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

import nested_admin

from covid.models import CovidUserDetail
from user.models import City, State, User


class CovidUserDetailInline(nested_admin.NestedTabularInline):
    model = CovidUserDetail
    extra = 0


class UserResource(resources.ModelResource):
    class Meta:
        model = User


class UserAdmin(nested_admin.NestedModelAdmin, ImportExportModelAdmin):
    resource_class = UserResource
    inlines = [CovidUserDetailInline, ]
    list_display = ('name', 'gender', 'dob', 'city', 'contact_number',
                    'created_at', )
    list_filter = ('gender', 'city', )
    search_fields = ('id', 'name', 'contact_number')


admin.site.register(State)
admin.site.register(City)
admin.site.register(User, UserAdmin)
