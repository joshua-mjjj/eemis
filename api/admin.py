from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin

from api.models import (
    User,
    RecruitmentAgency,
    Worker
    
)

admin.site.site_header = "EEMIS"
admin.site.index_title = "EEMIS Dashboard"


admin.site.register(User)
admin.site.register(RecruitmentAgency)
admin.site.register(Worker)

