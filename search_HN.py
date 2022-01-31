import requests
import time


def top_posts(hn_num):
    # トップ画面の投稿の各IDを取得
    posts_id = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    post_num = posts_id.json()[0:hn_num]
    # 下のURLで1件毎の情報取得可能⇒{}内に各IDを格納したい
    # post = requests.get('https://hacker-news.firebaseio.com/v0/item/{ID}.json')

    posts = []
    for post in post_num:
        url = f"https://hacker-news.firebaseio.com/v0/item/{post}.json"
        post_get = requests.get(url)
        time.sleep(1)
        title = post_get.json()['title']
        link = post_get.json()['url']
        posts.append(f"'title': '{title}', 'link': '{link}'")

    return posts
