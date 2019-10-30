import requests
import os

def write_images(subreddit, image_dict):
    image_list = []
    directory = os.path.dirname(f"visual_reddit/static/visual_reddit/images/{subreddit}/")
    if not os.path.exists(directory):
        os.makedirs(directory)

    for submission_id, value in image_dict.items():
        print(value)
        url = value[0]
        title = value[1]
        image = requests.get(url)
        with open(f"{directory}/{submission_id}", 'wb') as f:
            f.write(image.content)
            static_path = "/".join(str(f.name).split("/")[2:])
            image_list.append(f"{static_path}|{title}")

    return image_list