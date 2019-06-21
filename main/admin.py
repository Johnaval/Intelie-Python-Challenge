from django.contrib import admin
from .models import Schema, Entry
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

'''class TutorialAdmin(admin.ModelAdmin):
    fields = ["tutorial_title",
              "tutorial_content",
              "Ttutorial_published"]

    fieldsets = [("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
                ("URL", {'fields':['tutorial_slug']}),
                ('Series', {'fields':['tutorial_series']}),
                ("Content", {"fields":["tutorial_content"]}),
                 ]

    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()}
        }

class EntityAdmin(admin.ModelAdmin):
    fieldsets = [("Name", {"fields":["entity_name"]}),
                ("Address", {"fields":["entity_address"]}),
                ]'''
admin.site.register(Schema)
admin.site.register(Entry)