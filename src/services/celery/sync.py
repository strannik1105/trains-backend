import json
from datetime import datetime, timedelta
from uuid import uuid4

import psycopg2
from services.celery.celery_app import celery_app
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@celery_app.task()
def collect_data():
    # секунда, чтобы учесть time penalty при запуске задачи воркером

    with celery_app.producer_pool.acquire(block=True) as producer:
        # TODO: проработать запрос данных по конкретным вагонам и поездам
        producer.publish(
            {'messge': 'update'},
            routing_key='mock_parser',
            exchange="amq.direct",
            message_id=uuid4().hex,
            content_type="application/json",
        )
