from django.db import models
from django.utils import timezone
from django.utils.translation import get_language


class Category(models.Model):
    name_en = models.CharField(max_length=100)
    name_zh = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name_en']

    def __str__(self):
        return self.name_en

    @property
    def name(self):
        lang = get_language() or 'en'
        return self.name_zh if lang.startswith('zh') else self.name_en


class Tag(models.Model):
    name_en = models.CharField(max_length=50)
    name_zh = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name_en']

    def __str__(self):
        return self.name_en

    @property
    def name(self):
        lang = get_language() or 'en'
        return self.name_zh if lang.startswith('zh') else self.name_en


class Article(models.Model):
    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
    ]

    title_en = models.CharField(max_length=200)
    title_zh = models.CharField(max_length=200, blank=True)
    content_en = models.TextField(help_text='Write in Markdown')
    content_zh = models.TextField(blank=True, help_text='Write in Markdown')
    cover_image = models.ImageField(upload_to='articles/', blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles'
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_DRAFT)
    slug = models.SlugField(unique=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title_en

    def save(self, *args, **kwargs):
        if self.status == self.STATUS_PUBLISHED and not self.published_at:
            self.published_at = timezone.now()
        elif self.status == self.STATUS_DRAFT:
            self.published_at = None
        super().save(*args, **kwargs)

    @property
    def title(self):
        lang = get_language() or 'en'
        if lang.startswith('zh') and self.title_zh:
            return self.title_zh
        return self.title_en

    @property
    def content(self):
        lang = get_language() or 'en'
        if lang.startswith('zh') and self.content_zh:
            return self.content_zh
        return self.content_en
