from django.contrib import admin
from .models import Category, Tag, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_zh', 'slug']
    prepopulated_fields = {'slug': ('name_en',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_zh', 'slug']
    prepopulated_fields = {'slug': ('name_en',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'status', 'category', 'published_at', 'created_at']
    list_filter = ['status', 'category', 'tags']
    search_fields = ['title_en', 'title_zh', 'content_en', 'content_zh']
    prepopulated_fields = {'slug': ('title_en',)}
    filter_horizontal = ['tags']
    readonly_fields = ['created_at', 'updated_at', 'published_at']
    fieldsets = (
        ('English Content', {
            'fields': ('title_en', 'content_en'),
        }),
        ('Chinese Content', {
            'fields': ('title_zh', 'content_zh'),
            'classes': ('collapse',),
        }),
        ('Meta', {
            'fields': ('slug', 'status', 'cover_image', 'category', 'tags'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'published_at'),
            'classes': ('collapse',),
        }),
    )
