from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import mysql_url
from app.models.article import *


class ArticleOrm:
    def __init__(self) -> None:
        engine = create_engine(
            mysql_url,
            encoding="utf-8",
            echo=True
        )

        # self.DBSession = sessionmaker(bind=engine)
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def get_article_list(self):
        # with self.DBSession() as session:
        data = self.session.query(Article.article_id).all()
        total = 10
        self.session.close()
        return data, total
