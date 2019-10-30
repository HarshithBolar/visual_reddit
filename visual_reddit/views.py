from django.http import HttpResponse
from django.template import loader
from .api import reddit_api
from .api import redis_api
from .api import image_api

reddit_api = reddit_api.MyReddit()
redis_api = redis_api.MyRedis()

def fetch_images_from_cache(cached_images):
    cached_image_dict = {}
    for entry in cached_images:
        path, title = entry.split("|")
        submission_id = path.split("/")[-1]
        cached_image_dict[submission_id] = (path, title)
    return cached_image_dict

def search(request):
    keyword = request.GET.get('keyword')
    template = loader.get_template('visual_reddit/index.html')
    image_dict = reddit_api.search(keyword)
    context = {
        'image_dict': image_dict
    }

    return HttpResponse(template.render(context, request))

def index(request, subreddit='all'):
    cached_images = redis_api.retrieve(subreddit)
    template = loader.get_template('visual_reddit/index.html')

    if cached_images is not None:
        print(cached_images)
        cached_image_dict = fetch_images_from_cache(eval(cached_images))
        print(cached_image_dict)
        context = {
            'image_dict': cached_image_dict
        }
    else:
        image_dict = reddit_api.get_top_images(subreddit)
        image_list = image_api.write_images(subreddit, image_dict)
        redis_api.store(subreddit, str(image_list), 60)
        context = {
            'image_dict': image_dict
        }

    return HttpResponse(template.render(context, request))
