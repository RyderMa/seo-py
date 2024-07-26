from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import mysql_url
from app.models.model import *
from utils import connection
from fastapi import Request


class AppOrm:
    def __init__(self) -> None:
        self.engine = create_engine(
            mysql_url,
            encoding="utf-8",
            echo=True
        )

        self.DBSession = sessionmaker(bind=self.engine)
        self.connection = connection

    def get_app_list(self, request: Request):
        with self.connection(self.DBSession) as session:

            # return data, total
            return None

    def get_app_detail(self, request: Request):
        with self.connection(self.DBSession) as session:
            return None

    def get_app_template(self, request: Request):
        with self.connection(self.DBSession) as session:
            # return data
            return None

    def get_app_category(self, request: Request):
        with self.connection(self.DBSession) as session:
            # return data
            return None
