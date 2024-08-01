from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import mysql_url
from app.models.model import *
from utils import connection
from fastapi import Request
import json

PAGE_SIZE = 12


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
            params = request.query_params
            page = int(params.get('current', 1))
            pageSize = int(params.get('pageSize', PAGE_SIZE))

            res = session.query(App).filter(App.delete_flag == 0).offset(
                (page - 1)*pageSize).limit(pageSize)

            data = res.all()
            total = res.count()

            return data, total

    def get_app_detail(self, request: Request):
        with self.connection(self.DBSession) as session:
            params = request.query_params
            appId = params.get('appId', '')

            res = session.query(App).with_entities(
                App.app_id, App.app_name, App.first_api, App.description, App.keywords).filter(
                    App.app_id == appId).all()
            res = [{'app_id': app_id, "app_name": name, "first_api": first_api, "description": description,
                    "keywords": keywords} for app_id, name, first_api, description, keywords in res]

            data = res[0] if len(res) > 0 else None

            return data

    def get_app_template(self, request: Request):
        with self.connection(self.DBSession) as session:
            params = request.query_params
            appId = params.get('appId', '')

            res = session.query(AppTemplate).filter(
                AppTemplate.app_id == appId, AppTemplate.delete_flag == 0).all()

            data = []
            for app in res:
                try:
                    config = json.loads(app.config)
                except:
                    config = app.config or None
                data.append({
                    'template_id': app.template_id, 'config': config,
                    'name': app.template.template_name, 'key': app.template.key})

            return data

    # def getTemplateDetail(self, request):
    #     with self.connection(self.DBSession) as session:
    #         params = request.query_params
    #         templateId = params.get('templateId', '')

    #         res = session.query(Template).filter(
    #             Template.template_id == templateId).filter(Template.delete_flag == 0)
    #         data = res.all()

    #         return data

    def get_app_category(self, request: Request):
        with self.connection(self.DBSession) as session:
            params = request.query_params
            appId = params.get('appId', '')

            res = session.query(DictArticleType).with_entities(
                DictArticleType.sort, DictArticleType.name, DictArticleType.level, DictArticleType.key, DictArticleType.dict_article_type_id).filter(
                DictArticleType.app_id == appId, DictArticleType.delete_flag == 0).order_by(
                    DictArticleType.sort).all()

            data = []
            for category in res:
                data.append({
                    'id': category.dict_article_type_id,
                    'sort': category.sort, 'name': category.name,
                    'level': category.level, 'key': category.key})

            return data
