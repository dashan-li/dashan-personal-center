import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.http import JsonResponse
from django.contrib.auth.models import User


def debug_view(request):
    db_url = os.environ.get("DATABASE_URL", "")
    db_cfg = settings.DATABASES.get("default", {})
    try:
        user_count = User.objects.count()
        users = list(User.objects.values("username", "is_staff", "is_superuser", "is_active"))
        db_ok = True
        db_err = None
    except Exception as e:
        user_count = -1
        users = []
        db_ok = False
        db_err = str(e)
    return JsonResponse({
        "settings_module": os.environ.get("DJANGO_SETTINGS_MODULE"),
        "debug": settings.DEBUG,
        "database_url_present": bool(db_url),
        "database_url_prefix": db_url[:40] if db_url else None,
        "db_engine": db_cfg.get("ENGINE"),
        "db_name": str(db_cfg.get("NAME", ""))[:60],
        "db_connection_ok": db_ok,
        "db_error": db_err,
        "user_count": user_count,
        "users": users,
    })


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('debug/', debug_view),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('blog/', include('apps.blog.urls')),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
