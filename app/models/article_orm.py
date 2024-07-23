from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import mysql_url
from app.models.article import *
from utils import connection
from fastapi import Request


class ArticleOrm:
    def __init__(self) -> None:
        self.engine = create_engine(
            mysql_url,
            encoding="utf-8",
            echo=True
        )

        self.DBSession = sessionmaker(bind=self.engine)
        self.connection = connection

    def get_article_list(self, request: Request):
        with self.connection(self.DBSession) as session:
            query = request.query_params
            print("---------Getting article list---------", query)
            data = session.query(Article).all()
            total = len(data)
            return data, total
