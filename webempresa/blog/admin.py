from django.contrib import admin
from .models import Category,Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(Category,CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    list_display=("title","author","published")
    ordering=("author","published")
    search_fields=("title","content")
    date_hierarchy="published"
    list_filter=("author__username",)
    
admin.site.register(Post,PostAdmin)