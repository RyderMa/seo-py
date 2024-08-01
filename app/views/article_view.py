from app.controllers.article_controller import ArticleController
from utils import get_resp


class ArticleView():
    @staticmethod
    async def get(request):
        controller = ArticleController()
        data, total = controller.get_article_list(request)
        return get_resp(data={'list': data, 'total': total})

    @staticmethod
    async def post(request):
        request_body = await request.json()
        print('post', request_body)

class ArticleDetailView():
    @staticmethod
    async def get(request):
        controller = ArticleController()
        data = controller.get_article_detail(request)
        return get_resp(data=data)