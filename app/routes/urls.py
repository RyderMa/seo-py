from fastapi import FastAPI
from app.views.app_api import *
from app.views.article_api import *


def init_app_url(app: FastAPI):
    app.add_api_route("/app", app_manage, methods=['GET'])
    app.add_api_route("/app/detail", app_detail_manage, methods=["GET"])
    app.add_api_route("/app/template", app_template_manage, methods=["GET"])
    app.add_api_route("/app/category", app_category_manage, methods=["GET"])
    app.add_api_route("/article", article_manage, methods=["GET", "POST"])
    app.add_api_route("/article/detail", article_detail_manage, methods=["GET"])
