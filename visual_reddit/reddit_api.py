import praw

class MyReddit:
    def __init__(self):
        self.reddit = praw.Reddit('visual-reddit', user_agent='visual_reddit_1.0')