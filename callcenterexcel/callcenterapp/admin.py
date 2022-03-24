# from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from callcenterapp.models import Customerdetails,  Status, User

# @admin.register(Customerdetails)
# class CustomerdetailsAdmin(ImportExportModelAdmin):
#     list_display=('name','phone' )

# Register your models here.
admin.site.register(User)
admin.site.register(Customerdetails)
admin.site.register(Status)

