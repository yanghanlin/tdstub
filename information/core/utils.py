from ..models import Instance, Event, EventTag
from pathlib import Path
from django.conf import settings
from typing import Union, Iterable
from os import PathLike
from uuid import uuid4
from datetime import datetime
from django.utils import timezone


def instance_local(path: Union[str, PathLike]) -> Path:
    instance_local_dir = settings.BASE_DIR / 'instance-local'
    if not instance_local_dir.exists():
        instance_local_dir.mkdir(parents=True, exist_ok=True)
    return instance_local_dir / path


def current_instance() -> Instance:
    try:
        with open(instance_local('current-instance-uid'), 'r', encoding='utf-8') as file:
            uid = file.read()
        instance = Instance.objects.get(uid=uid)
        return instance
    except (FileNotFoundError, Instance.DoesNotExist):
        init_time = datetime.now().isoformat()
        instance = Instance(uid=str(uuid4()), description='Instance initialized at {}'.format(init_time))
        instance.save()
        record_event(
            'Instance {} initialized at {}'.format(instance.uid, init_time),
            'instance.init',
            instance=instance
        )
        with open(instance_local('current-instance-uid'), 'w', encoding='utf-8') as file:
            file.write(instance.uid)
        return instance


def record_event(description: str, tags: Union[str, Iterable] = (), *, instance: Instance = None):
    if instance is None:
        instance = current_instance()
    if isinstance(tags, str):
        tags = (tags,)
    event = Event(description=description, timestamp=timezone.now(), instance=instance)
    event.save()
    tag_objects = []
    for tag in tags:
        try:
            tag_objects.append(EventTag.objects.get(name=tag))
        except EventTag.DoesNotExist:
            tag_object = EventTag(name=tag)
            tag_object.save()
            tag_objects.append(tag_object)
    for tag_object in tag_objects:
        event.tags.add(tag_object)
    return event
