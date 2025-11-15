from django.shortcuts import get_object_or_404

from .models import Echo


class EchoConverter:
    regex = r'\d+'

    def to_python(self, echo_id: str) -> Echo:
        return get_object_or_404(Echo, id=int(echo_id))

    def to_url(self, echo: Echo) -> int:
        return echo.id
