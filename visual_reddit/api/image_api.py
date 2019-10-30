import requests
import os
from PIL import Image
from io import BytesIO


def write_images(subreddit, image_dict):
    image_list = []
    dirname = f"visual_reddit/static/visual_reddit/images/{subreddit}/"
    directory = os.path.dirname(dirname)
    if not os.path.exists(directory):
        os.makedirs(directory)

    for submission_id, value in image_dict.items():
        print(value)
        url = value[0]
        title = value[1]
        req = requests.get(url)
        im_downsized = downsize(req)

        filepath = f"{directory}/{submission_id}"
        im_downsized.save(filepath + ".jpg")
        static_path = "/".join(filepath.split("/")[2:])
        image_list.append(f"{static_path}|{title}")

    return image_list


def downsize(req):
    image = Image.open(BytesIO(req.content))
    image = image.convert('RGB')
    return image.resize((400, 400))
