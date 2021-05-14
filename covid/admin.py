from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

import nested_admin

from covid.models import *


class CovidUserDetailResource(resources.ModelResource):
    class Meta:
        model = CovidUserDetail


class CovidUserDetailAdmin(nested_admin.NestedModelAdmin,
                           ImportExportModelAdmin):
    resource_class = CovidUserDetailResource
    list_display = ('user', 'user_type', 'blood_group',
                    'covid_positive_date', 'covid_negate_date',
                    'is_verified', )
    list_filter = ('user_type', 'blood_group', 'is_verified', )
    search_fields = ('id', 'user__id', )


admin.site.register(Referrer)
admin.site.register(CovidUserDetail, CovidUserDetailAdmin)
