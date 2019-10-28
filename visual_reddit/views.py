from django.http import HttpResponse
from django.template import loader
from . import reddit_api

reddit_api = reddit_api.MyReddit()

def search(request):
    keyword = request.GET.get('keyword')
    template = loader.get_template('visual_reddit/index.html')
    image_dict = reddit_api.search(keyword)
    context = {
        'image_dict': image_dict
    }

    return HttpResponse(template.render(context, request))

def index(request, subreddit='all'):
    image_dict = reddit_api.get_top_images(subreddit)
    template = loader.get_template('visual_reddit/index.html')
    context = {
        'image_dict': image_dict
    }

    return HttpResponse(template.render(context, request))
