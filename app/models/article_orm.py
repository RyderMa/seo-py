from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import mysql_url
from app.models.model import *
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
            params = request.query_params
            type = params.get('type')
            page = int(params.get('page') or 1)
            res = session.query(Article).join(
                ArticleImg, ArticleImg.article_id == Article.article_id, isouter=True).join(
                    DictArticleType, DictArticleType.dict_article_type_id == Article.type_level_1).filter(
                        Article.delete_flag == 0)

            if (type):
                res = res.filter(Article.type_level_1 == type)

            res = res.order_by(Article.add_time.desc())
            total = res.count()
            data = res.offset((page - 1) * 12).limit(12).all()

            return data, total

    def get_article_detail(self, request: Request):
        with self.connection(self.DBSession) as session:
            params = request.query_params
            article_id = params.get('article_id')

            data = {"detail": None}
            res = session.query(ArticleDetail).filter(
                ArticleDetail.article_id == article_id).all()

            if (len(res) > 0):
                data['detail'] = res[0]

            return data
