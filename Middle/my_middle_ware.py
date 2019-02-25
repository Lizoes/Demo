from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class my_middle_ware_1(MiddlewareMixin):
    def process_request(self, request):
        print("in the my_middle_ware_1 request")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("in the my_middle_ware_1 view")


    def process_response(self, request, response):
        print("in the my_middle_ware_1 response")
        return response


class my_middle_ware_2(MiddlewareMixin):
    def process_request(self, request):
        print("in the my_middle_ware_2 request")
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("in the my_middle_ware_2 view")
    def process_response(self, request, response):
        print("in the my_middle_ware_2 response")
        return response


class my_middle_ware_3(MiddlewareMixin):
    def process_request(self, request):
        print("in the my_middle_ware_3 request")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("in the my_middle_ware_3 view")


    def process_response(self, request, response):
        print("in the my_middle_ware_3 response")
        return response

