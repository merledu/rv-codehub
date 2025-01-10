# from django.contrib import admin
# from .models import *
# # Register your models here.

# admin.site.register(BugReport)


from django.contrib import admin

from .models import BugReport




class BugReportAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'severity', 'created_at')



admin.site.register(BugReport, BugReportAdmin)