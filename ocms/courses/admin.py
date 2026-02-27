from django.contrib import admin
from .models import Category, Course, Module, Lecture

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'instructor', 'category', 'price')
    list_filter = ('category', 'instructor')
    search_fields = ('title', 'description')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'order')
    list_filter = ('course',)
    search_fields = ('title',)

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'module', 'order')
    list_filter = ('module',)
    search_fields = ('title',)
