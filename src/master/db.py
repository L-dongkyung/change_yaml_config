import logging
import time
import json
import os

from fastapi import FastAPI
import mongoengine
from mongoengine.connection import disconnect


class Mongo:
    def __init__(self, app: FastAPI = None, **kwargs):
        if app is not None:
            self.init_app(app=app, **kwargs)

    def init_app(self, app: FastAPI, **kwargs):
        """
        connect db
        """

        @app.on_event("startup")
        def startup():
            for db_name in kwargs.get("DBS"):
                mongoengine.connect(
                    db_name,
                    host=kwargs.get("DB_HOST"),
                    port=kwargs.get("DB_PORT"),
                    connectTimeoutMS=kwargs.get("TIMEOUT"),
                    alias=db_name
                )

        @app.on_event("shutdown")
        def shutdown():
            for db_name in kwargs.get("DBS"):
                disconnect(alias=db_name)


db = Mongo()





