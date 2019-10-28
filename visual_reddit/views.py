from django.http import HttpResponse
from . import reddit_api

reddit_api = reddit_api.MyReddit()

def index(request):
    return HttpResponse("Display top 40 images from r/all")
