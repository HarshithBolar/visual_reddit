import praw

class MyReddit:
    valid_image_extensions = ('jpg', 'jpeg', 'png', 'gif')

    def __init__(self):
        self.reddit = praw.Reddit('visual-reddit', user_agent='visual_reddit_1.0')

    def get_image_submissions(self, submissions):
        post_map = {}
        image_counter = 0

        for submission in submissions:
            if str(submission.url).endswith(self.valid_image_extensions):
                post_map[str(submission)] = (str(submission.url), submission.title)
                image_counter += 1
            if image_counter >= 28:
                break

        return post_map

    def search(self, keyword):
        results = self.reddit.subreddit('all').search(keyword, sort='relevance', limit=None, time_filter='day')
        post_map = self.get_image_submissions(results)
        return post_map

    def get_top_images(self, subreddit):
        post_map = self.get_image_submissions(self.reddit.subreddit(subreddit).hot(limit=None))
        return post_map
