from app.controllers.app_controller import *


class AppView():
    @staticmethod
    async def get(request):
        controller = AppController()
        return controller.get_app_list(request)


class AppDetailView():
    @staticmethod
    async def get(request):
        controller = AppController()
        return controller.get_app_detail(request)


class AppTemplateView():
    @staticmethod
    async def get(request):
        controller = AppController()
        return controller.get_app_template(request)


class AppCategoryView():
    @staticmethod
    async def get(request):
        controller = AppController()
        return controller.get_app_category(request)
