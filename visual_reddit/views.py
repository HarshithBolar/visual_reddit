from django.http import HttpResponse
from django.template import loader
from . import reddit_api

reddit_api = reddit_api.MyReddit()

def index(request):
    image_dict = reddit_api.get_top_40_images()
    template = loader.get_template('visual_reddit/index.html')

    context = {
        'image_dict': image_dict
    }

    return HttpResponse(template.render(context, request))
