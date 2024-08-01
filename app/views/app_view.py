from app.controllers.app_controller import *
from utils import get_resp


class AppView():
    @staticmethod
    async def get(request):
        controller = AppController()
        data, total = controller.get_app_list(request)
        return get_resp(data={"list": data, 'total': total})


class AppDetailView():
    @staticmethod
    async def get(request):
        controller = AppController()
        data = controller.get_app_detail(request)
        return get_resp(data=data)


class AppTemplateView():
    @staticmethod
    async def get(request):
        controller = AppController()
        data = controller.get_app_template(request)
        return get_resp(data=data)


class AppCategoryView():
    @staticmethod
    async def get(request):
        controller = AppController()
        data = controller.get_app_category(request)
        return get_resp(data=data)
