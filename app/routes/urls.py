from fastapi import FastAPI
from app.views.article_api import *


def init_app_url(app: FastAPI):
    app.add_api_route("/article", article_manage,
                      methods=["GET", "POST"])
