# Visual Reddit 

#### An image feed for Reddit with subreddit and keyword based search

<p align="center">
  <img width="700" src="https://i.imgur.com/K6IligW.jpg">
</p>

Visual Reddit fetches images from Reddit and displays them in a grid like format stripping off all the additional noise. Clicking on the image will take you to the corresponding Reddit post. The first screenshot shows images from the subreddit [/r/Wallpapers](https://www.reddit.com/r/wallpapers/) and the second image a search result for the keyword 'sunset'.

Visual Reddit is written in Python and uses [Django](https://www.djangoproject.com/) as the backend. It uses [PRAW](https://github.com/praw-dev/praw) for communicating with Reddit, [Redis](https://redis.io/) for caching images/image links, [Redis Queues](https://python-rq.org/) for running background tasks and [Pillow](https://pillow.readthedocs.io/en/stable/) for server side resizing.

Installation
------------
#### Tools and dependency managers
* `Python 3`
* `pip` for Python 3 
* `git`

#### Setup the project
1. Clone the repository. 
   ```
   git clone https://github.com/HarshithBolar/visual_reddit.git
   ```
2. Using a terminal editor, change your current directory to top level of the cloned repository and create a virtual environment and activate it. If virtualenv not found, install it first - https://virtualenv.pypa.io/en/latest/installation/
   ```
   cd visual_reddit
   virtualenv venv
   source venv/bin/activate
   ```
3. Install all required dependencies using pip
   ```
   pip install -r requirements.txt
   ```
4. Create an API token and secret key for your app on Reddit. Create a `praw.ini` file in the top level directory with this information - [help](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html#defining-additional-sites). Give it the name `visual-reddit`.
5. Install Redis.
   ```
   wget http://download.redis.io/releases/redis-5.0.7.tar.gz
   tar xzf redis-5.0.7.tar.gz
   cd redis-5.0.7
   make
   ```
6. Start `redis-server`. It runs on port 6379 by default.
   ```
   redis-5.0.7/src/redis-server
   ```
7. Start `rq` worker from the top level directory.
   ```
   venv/bin/rq worker
   ```
8. Start Django development server. Visual Reddit should be accessible on port 8000.
   ```
   python manage.py runserver
   ```

License
-------
Visual Reddit is provided under the [Simplified BSD License](https://github.com/HarshithBolar/visual_reddit/blob/master/LICENSE.md)
