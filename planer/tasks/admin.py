from django.contrib import admin
from .models import Tasks


class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'task')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'task')


admin.site.register(Tasks, TasksAdmin)
