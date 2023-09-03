import sys

sys.path.append(".")
from src.common.api_svc_settings import APISettings


class SchemaStorageAPISettings(APISettings):
    svc_name: str = "schema_storage_api"
    #: строка коннекта к RabbitMQ
    amqp_url: str = "amqp://crwl:Crawly97@rabbitmq/"

    #: обменник для публикаций
    publish: dict = {
        "main": {
            "name": "crawly",
            "type": "direct",
            "routing_key": "schema_storage_api_publish"
        }
    }
    consume: dict = {
        "queue_name": "schema_storage_api_consume",
        "exchanges": {
            "main": {
                #: имя обменника
                "name": "crawly",
                #: тип обменника
                "type": "direct",
                #: привзяка для очереди
                "routing_key": ["schema_storage_api_consume"]
            }
        }
    }

