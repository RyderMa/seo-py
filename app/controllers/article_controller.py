from app.models.article_orm import ArticleOrm


class ArticleController():
    def __init__(self):
        self.model = ArticleOrm()

    def get_article_list(self):
        data, total = self.model.get_article_list()

        return data, total
