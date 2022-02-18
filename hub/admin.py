from operator import truediv
from re import search
from tkinter import VERTICAL
from django.contrib import admin,messages
from .models import User, Student, Coach, memberShip,Project

# Register your models here.

class ProjectInline(admin.TabularInline):
    model = Project


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = (
         "last_name",
        "first_name"
    )
    fields =[ ("last_name","first_name"),
            "email"
    ]
    search_fields = ["last_name","first_name"]

class StutendtAdmin(admin.ModelAdmin):
    list_display = (
         "last_name",
        "first_name"
    )
    fields =[ ("last_name","first_name"),
            "email"
    ]
    search_fields = ["last_name","first_name"]
    inlines = [ProjectInline]


class ProjectDurationFilter(admin.SimpleListFilter):
    parameter_name = 'duration'
    title = 'Durée'
    
    def lookups(self, request, model_admin):
        return(
            ('1 Month', 'less than 1 Month'),
            ('3 Months', 'less than 3 Months')
        )
        
    def queryset(self, request, queryset):
        if self.value() == "1 Month":
            return queryset.filter(duration__lte=30)
        if self.value() == "3 Months":
            return queryset.filter(duration__gt=30,duration__lte=90)




def set_Valid(modeladmin,request,queryset):
    rows = queryset.update(isValid=True)
    if rows ==1:
        msg = "1 project was"
    else:
        msg = f"{rows} projects were",
    messages.success(request, message=f"{msg} successfuly marked as valid")
    
set_Valid.short_description = "Validate"


def set_NonValid(modeladmin,request,queryset):
    rows = queryset.update(isValid=False)
    if rows ==1:
        msg = "1 project was"
    else:
        msg = f"{rows} projects were",
    messages.success(request, message=f"{msg} successfuly marked as Not Valid")
    
set_NonValid.short_description = "Invalidate"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    actions = [set_Valid,set_NonValid]
    actions_on_bottom = True 


    list_filter = (
        'creator',
        'isValid',
        ProjectDurationFilter
    )


    list_display = (
        'name',
        'duration',
        'supervisor',
        'creator',
        'isValid'
    )
    fieldsets = [
        (
            'state',
            {
                'fields':('isValid',)
            }
        ),
        (
            'about',
            {
                'fields':(
                'name',
                ('creator','supervisor'),
                'besoin',
                'desc')
            }
        ),
        (
            'Durations',
            {
                'classes': ('collapse',),
                'fields': (
                    'duration',
                    'time_allocated'
                )
            }
        )
    ]
  #  radio_fields = { "supervisor" :  admin.VERTICAL}
    autocomplete_fields = ['supervisor']
    empty_value_display = '-empty-'
 #   readonly_fields = ''

admin.site.register(Student,StutendtAdmin)
#admin.site.register(Coach,CoachAdmin)
#admin.site.register(Project)
admin.site.register(memberShip)
