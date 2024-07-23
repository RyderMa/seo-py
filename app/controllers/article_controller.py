from app.models.article_orm import ArticleOrm


class ArticleController():
    def __init__(self):
        self.model = ArticleOrm()

    def get_article_list(self, request):
        data, total = self.model.get_article_list(request)

        return data, total
