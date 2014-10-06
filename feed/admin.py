from django.contrib import admin
from feed import models

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'content',
        'published_at',
    ]

admin.site.register(models.Post, PostAdmin)

