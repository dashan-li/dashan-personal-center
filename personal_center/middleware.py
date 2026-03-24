import logging
import json

logger = logging.getLogger('django.request')


class LoginDebugMiddleware:
    """Log everything about admin login requests to diagnose auth failures."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        is_login = request.path.endswith('/admin/login/')

        if is_login:
            logger.warning(
                f"[LOGIN DEBUG] {request.method} {request.path} | "
                f"Host: {request.get_host()} | "
                f"Proto: {request.META.get('HTTP_X_FORWARDED_PROTO', 'none')} | "
                f"is_secure: {request.is_secure()} | "
                f"session_key: {request.session.session_key} | "
                f"cookies: {list(request.COOKIES.keys())}"
            )
            if request.method == 'POST':
                logger.warning(
                    f"[LOGIN POST] username={request.POST.get('username')} | "
                    f"has_password={bool(request.POST.get('password'))} | "
                    f"csrftoken_in_cookie={bool(request.COOKIES.get('csrftoken'))} | "
                    f"csrftoken_in_post={bool(request.POST.get('csrfmiddlewaretoken'))}"
                )

        response = self.get_response(request)

        if is_login:
            logger.warning(
                f"[LOGIN RESPONSE] status={response.status_code} | "
                f"set_cookie_headers={[k for k in response.items() if k[0].lower() == 'set-cookie']}"
            )
            if request.method == 'POST':
                logger.warning(
                    f"[LOGIN POST RESULT] user_authenticated={request.user.is_authenticated} | "
                    f"user={getattr(request.user, 'username', 'anonymous')}"
                )

        return response
