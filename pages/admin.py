from django.contrib import admin
from .models import UserCategory, VacationSlot, UserVacation
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(UserCategory)
class UserCategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(VacationSlot)
class VacationSlotAdmin(ImportExportModelAdmin):
    pass

@admin.register(UserVacation)
class UserVacationAdmin(ImportExportModelAdmin):
    pass