import praw
import time

r = praw.Reddit(user_agent = "God of Sleep by Bryan /u/GOD_OF_SLEEP")
print("Logging in")
r.login()

words_to_match = ["holy", "jesus", "christ", "god"]
cache = []

def run_bot():
    print("Grabbing subreddit")
    subreddit = r.get_subreddit("nosleep")
    print("Grabbing comments")
    comments = subreddit.get_comments(limit=25)
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in cache and isMatch:
            print("Match found. Comment ID:" + comment.id)
            comment.reply("Hello. I am the God of Sleep. I hear that you called for me. I will bless you tonight. You'll need it.")
            cache.append(comment.id)

    print("Comment loop finished. Time to sleep.")
while True:
    run_bot()
    time.sleep(10)
