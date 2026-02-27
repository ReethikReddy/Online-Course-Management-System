from django.contrib import admin
from .models import Enrollment, Progress

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'enrolled_at')
    list_filter = ('course', 'enrolled_at')
    search_fields = ('student__username', 'course__title')

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'enrollment', 'lecture', 'completed_at')
    list_filter = ('lecture__module__course',)
