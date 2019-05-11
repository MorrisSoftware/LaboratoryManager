from django.contrib import admin
import datetime
from .models import CalenderSetting, Instrument, InstrumentCategory, Reservation

import csv

def ExportAsCSV(modeladmin,request,queryset):
    ExportAsCSV.short_description = "Export selected entries as CSV"
    
    fields = queryset.model._meta.get_fields()

    with open(str(datetime.datetime.now()).replace(' ','_') + '_'+ str(queryset.model)+'.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        # write your header first
        for obj in queryset.model.objects.all():
            row = ""
            values = []
            for field in fields:
                value = getattr(obj, field.name)
                print(str(value))
                values.append(str(value))
                print(values)
            row = ",".join(values)
            print(row)
        writer.writerow(row)

@admin.register(CalenderSetting)
class ReservationCalenderSettingsAdmin(admin.ModelAdmin):
    list_display = ['setting_name','active']
    fields = ['setting_name','number_of_days','first_session_time','time_interval','number_of_sessions','active']

@admin.register(InstrumentCategory)
class InstrumentCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    
    list_display = ['instrument_name','manufacturer','model','year', 'under_maintenance']
    list_filter = ('category','under_maintenance')
    fields = ['category','instrument_name','manufacturer','model','year','location','image','under_maintenance']

@admin.register(Reservation) 
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user_id','instrument_id','date', 'time_start','time_end' ]
    fields = ['user_id','instrument_id','date', 'time_start','time_end' ]       
    actions=[ExportAsCSV]