from django.http import HttpResponse
from django.template import loader
from rq import Queue

from .api import image_api
from .api import reddit_api
from .api import redis_api
import shutil
import os


reddit_api = reddit_api.MyReddit()
redis_api = redis_api.MyRedis()
task_queue = Queue(connection=redis_api.db)


def cache_images(subreddit, image_dict):
    image_list = image_api.write_images(subreddit, image_dict)
    redis_api.store(subreddit, str(image_list), 600)


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
        cached_image_dict = redis_api.fetch_images_from_cache(eval(cached_images))
        print(cached_image_dict)
        context = {
            'image_dict': cached_image_dict
        }
    else:
        image_dict = reddit_api.get_top_images(subreddit)
        if task_queue.fetch_job(subreddit) is None:
            static_path = f"visual_reddit/static/visual_reddit/images/{subreddit}/"
            if os.path.exists(static_path):
                shutil.rmtree(static_path)
            task_queue.enqueue(cache_images, subreddit, image_dict, job_id=subreddit)

        context = {
            'image_dict': image_dict
        }

    return HttpResponse(template.render(context, request))