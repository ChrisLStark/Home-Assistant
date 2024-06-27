DOMAIN = 'monkey_patch_nest_camera_event_end_date'
import logging
_LOGGER = logging.getLogger(__name__)

from nest.nest import CameraEvent
from datetime import timedelta

_pre_patch = CameraEvent.end_time

def end_time(self):
    time = self.pre_patch_end_time
    if time:
        return time + timedelta(seconds = 30)

CameraEvent.pre_patch_end_time = _pre_patch
CameraEvent.end_time = property(end_time)

def setup(hass, config):
    hass.states.set('monkeypatches.nest_camera_event_end_date_monkey_patch','true')
    _LOGGER.warning('MONKEYPATCH! Overriding python-nest CameraEvent end_time to add 30 seconds to events')
    return True