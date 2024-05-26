from django.contrib import admin
from .models import Comment, Category, Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Auto-populate slug field based on the title
    prepopulated_fields = {'slug': ('title',)}

    # List display options for the Post model in the admin panel
    list_display = ('title', 'author', 'created', 'updated', 'category')
    
    # Filter options for the Post model in the admin panel
    list_filter = ('created', 'updated', 'category')

    # Search fields for the Post model in the admin panel
    search_fields = ('title', 'body', 'author__username')
    
    # Date hierarchy navigation for the Post model in the admin panel
    date_hierarchy = 'created'

    # Fieldsets to organize fields in the admin form
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'body', 'image', 'category')
        }),
        ('Date Information', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)  # Collapse this section by default
        }),
    )

    # Automatically set the author field to the current user on save
    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)


