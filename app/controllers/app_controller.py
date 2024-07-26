from app.models.app_orm import *


class AppController():
    def __init__(self):
        self.model = AppOrm()

    def get_app_list(self, request):
        data, total = self.model.get_app_list(request)
        return data, total

    def get_app_detail(self, request):
        data = self.model.get_app_detail(request)
        return data

    def get_app_template(self, request):
        data = self.model.get_app_template(request)
        return data

    def get_app_category(self, request):
        data = self.model.get_app_category(request)
        return data
