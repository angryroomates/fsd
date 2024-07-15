from django.contrib import admin
from classapp.models import stud,course

admin.site.register(stud)
admin.site.register(course)

#@admin.register(course)

#class courseAdmin(admin.ModelAdmin):
    #list_display=('course_name',)
    #list_filter=('course_name',)
    #raw_id_fields=('student',)

#@admin.register(stud)
#class studAdmin(admin.ModelAdmin):
      # list_display=('fname','lname','email')
      # date_hierarchy='date_joined'
       #exclude=('lname',)
       #filter_horizontal=('students',)
       #raw_id_fields=('course',)

#admin.site.unregister(stud)
#admin.site.unregister(course)
#admin.site.register(stud,studAdmin)
#admin.site.register(course,courseAdmin)