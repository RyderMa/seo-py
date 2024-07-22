from fastapi import Request
from app.controllers.article_controller import ArticleController
from utils import get_resp


class ArticleView():
    @staticmethod
    async def get(request: Request):
        controller = ArticleController()
        data, total = controller.get_article_list()
        print('data', type(data))
        return get_resp(data={'data-list': data, 'total': total})

    @staticmethod
    async def post(request: Request):
        request_body = await request.json()
        print('post', request_body)
