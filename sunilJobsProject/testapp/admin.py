from django.contrib import admin
from testapp.models import HydJobs,BangJobs,PuneJobs
# Register your models here.
class HydAdmin(admin.ModelAdmin):
    list_display=['date','company','Title','eligibility','address','email','phonenumber']
class BangAdmin(admin.ModelAdmin):
    list_display=['date','company','Title','eligibility','address','email','phonenumber']
class PuneAdmin(admin.ModelAdmin):
    list_display=['date','company','Title','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HydAdmin)
admin.site.register(BangJobs,BangAdmin)
admin.site.register(PuneJobs,PuneAdmin)
