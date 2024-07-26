from fastapi import Request
from app.views.app_view import *


async def app_manage(request: Request):
    if request.method == 'GET':
        return await AppView.get(request)


async def app_detail_manage(request: Request):
    if request.method == 'GET':
        return await AppDetailView.get(request)


async def app_template_manage(request: Request):
    if request.method == 'GET':
        return await AppTemplateView.get(request)


async def app_category_manage(request: Request):
    if request.method == 'GET':
        return await AppCategoryView.get(request)
