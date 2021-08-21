"""Post admin."""


# django imports
from django.contrib import admin

# Register your models here.

# Local imports
from posts.models import Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ("pk", "user", "photo")