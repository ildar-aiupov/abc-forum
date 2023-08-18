from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import Q


class CheckActiveUsersMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        # обновить время активности текущего юзера
        if request.user.is_authenticated:
            request.user.last_activity = timezone.now()
            request.user.save()
        # расставить всем юзерам метки онлайн/неонлайн
        get_user_model().objects.update(
            is_online=Q(
                last_activity__gt=timezone.now() - timezone.timedelta(minutes=5)
            )
        )
        return None
