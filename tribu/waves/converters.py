from django.shortcuts import get_object_or_404

from .models import Wave


class WaveConverter:
    regex = r'\d+'

    def to_python(self, wave_id: str) -> Wave:
        return get_object_or_404(Wave, id=int(wave_id))

    def to_url(self, wave: Wave) -> int:
        return wave.id
