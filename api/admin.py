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

class UserAdmin(admin.ModelAdmin):
    list_display = ["home_address", "username", "contact", "occupation"]

class AgencyAdmin(admin.ModelAdmin):
    list_display = ["registered_name", "contact", "email"]

class WorkerAdmin(admin.ModelAdmin):
    list_display = ["full_name", "contact", "contract_start_date", "contract_end_date", "country_of_destination", "returned", "abroad"]

admin.site.register(User, UserAdmin)
admin.site.register(RecruitmentAgency, AgencyAdmin)
admin.site.register(Worker, WorkerAdmin)

