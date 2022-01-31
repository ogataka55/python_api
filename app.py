from search_HN import top_posts


def main():
    hn_num = int(input("トップページの上位何件を表示しますか？ > "))
    posts_main = top_posts(hn_num)
    for post_main in posts_main:
        print(post_main)


if __name__ == '__main__':
    main()
