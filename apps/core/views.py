from django.shortcuts import render
from django.utils.translation import get_language
from apps.blog.models import Article
from .experience_data import EXPERIENCE, INTERNSHIP, EDUCATION, SKILLS, PROFILE


def home(request):
    lang = 'zh' if get_language() and get_language().startswith('zh') else 'en'
    recent_articles = Article.objects.filter(status='published').order_by('-published_at')[:3]
    return render(request, 'core/home.html', {
        'profile': PROFILE[lang],
        'skills': SKILLS[lang],
        'experience': EXPERIENCE[lang],
        'internship': INTERNSHIP[lang],
        'education': EDUCATION[lang],
        'recent_articles': recent_articles,
        'lang': lang,
    })


def experience(request):
    lang = 'zh' if get_language() and get_language().startswith('zh') else 'en'
    return render(request, 'core/experience.html', {
        'experience': EXPERIENCE[lang],
        'internship': INTERNSHIP[lang],
        'education': EDUCATION[lang],
        'skills': SKILLS[lang],
        'lang': lang,
    })
