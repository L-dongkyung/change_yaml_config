import mongoengine


class Service(mongoengine.EmbeddedDocument):
    build = mongoengine.StringField(required=False)
    image = mongoengine.StringField(required=False)
    restart = mongoengine.StringField(required=False)
    ports = mongoengine.ListField(required=False)
    networks = mongoengine.ListField(required=False)
    volumes = mongoengine.ListField(required=False)
    environment = mongoengine.ListField(required=False)
    cpu_percent = mongoengine.IntField(required=False)
    mem_limit = mongoengine.StringField(required=False)
    links = mongoengine.ListField(required=False)
    command = mongoengine.StringField(required=False)


class Services(mongoengine.EmbeddedDocument):
    mongo = mongoengine.EmbeddedDocumentField(Service)
    rabbitmq = mongoengine.EmbeddedDocumentField(Service)
    master = mongoengine.EmbeddedDocumentField(Service)


class Server(mongoengine.EmbeddedDocument):
    driver = mongoengine.StringField(default="null", required=False)


class Network(mongoengine.EmbeddedDocument):
    optimserver = mongoengine.EmbeddedDocumentField(Server, null=True)


class Yml(mongoengine.Document):
    version = mongoengine.StringField()
    services = mongoengine.EmbeddedDocumentField(Services)
    networks = mongoengine.EmbeddedDocumentField(Network)

    meta = {
        "db_alias": 'yml',
        "indexes": ['services', ],
        "allow_inheritance": False,
    }



