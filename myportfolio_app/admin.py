from django.contrib import admin
from .models import Skill,Project,Contact

admin.site.register(Skill)
admin.site.register(Contact)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured")
    search_fields = ("title",)
    list_filter = ("featured",)