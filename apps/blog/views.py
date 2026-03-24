import mistune
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Category, Tag


def article_list(request):
    articles = Article.objects.filter(status='published')

    category_slug = request.GET.get('category')
    tag_slug = request.GET.get('tag')
    active_category = None
    active_tag = None

    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=active_category)
    if tag_slug:
        active_tag = get_object_or_404(Tag, slug=tag_slug)
        articles = articles.filter(tags=active_tag)

    paginator = Paginator(articles, 8)
    page = paginator.get_page(request.GET.get('page'))

    return render(request, 'blog/list.html', {
        'page': page,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'active_category': active_category,
        'active_tag': active_tag,
    })


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, status='published')
    md = mistune.create_markdown(plugins=['table', 'strikethrough', 'footnotes'])
    content_html = md(article.content)
    return render(request, 'blog/detail.html', {
        'article': article,
        'content_html': content_html,
    })
