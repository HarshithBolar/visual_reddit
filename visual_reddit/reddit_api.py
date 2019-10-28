import praw

class MyReddit:
    valid_image_extensions = ('jpg', 'jpeg', 'png', 'gif', 'gifv')

    def __init__(self):
        self.reddit = praw.Reddit('visual-reddit', user_agent='visual_reddit_1.0')

    def get_top_40_images(self, subreddit):
        post_map = {}
        image_counter = 0

        for submission in self.reddit.subreddit(subreddit).hot(limit=None):
            if str(submission.url).endswith(self.valid_image_extensions):
                post_map[str(submission)] = str(submission.url)
                image_counter += 1
            if image_counter >= 40:
                break

        return post_map
