from celery import Celery

import settings

celery_app = Celery(
    "services.device_sync.sync",
    broker=f"pyamqp://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@{settings.RABBITMQ_HOST}",
)
celery_app.conf.update(
    broker_connection_retry_on_startup=False,
    timezone="UTC",
    task_routes={
        "services.celery.sync.collect_data": "celery",
    },
    beat_schedule={
        "refresh-every-10-minutes": {
            "task": "services.device_sync.sync.collect_data",
            "schedule": 600.0,
        },
    },
)
