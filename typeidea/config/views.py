# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
# function
# def links(request):
#     if request.method =='GET':
#         return HttpResponse('GET')
# class
class Link(TemplateView):

    def get(self, request, *args, **kwargs):
        return HttpResponse('request')
