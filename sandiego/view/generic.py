# -*- coding:utf-8 -*-
# PROJECT_NAME : sandiego
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com
from abc import ABCMeta
from abc import abstractmethod


class AbastractBaseView(metaclass=ABCMeta):

    @abstractmethod
    def get(self, request):
        pass

    @abstractmethod
    def post(self, request):
        pass

    @abstractmethod
    def put(self, request):
        pass

    @abstractmethod
    def delete(self, request):
        pass


class BaseView(AbastractBaseView):

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

    pass


class TemplateBaseView(BaseView):
    pass


class TemplateView(TemplateBaseView):
    pass