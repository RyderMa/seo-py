from fastapi import Request
from app.views.article_view import ArticleView, ArticleDetailView


async def article_manage(request: Request):
    if request.method == "GET":
        return await ArticleView.get(request)
    elif request.method == "POST":
        return await ArticleView.post(request)
    else:
        return {"error": "Unsupported method"}

async def article_detail_manage(request: Request):
    if request.method == "GET":
        return await ArticleDetailView.get(request)
    else:
        return {"error": "Unsupported method"}