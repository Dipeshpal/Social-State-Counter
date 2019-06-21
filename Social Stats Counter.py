from bs4 import BeautifulSoup
import requests


def youtube():
    try:
        url = 'https://www.youtube.com/channel/UCGEoRAK92fUk2kY3kSJMR_Q'
    except:
        print("Channel  not found")

    temp = requests.get(url)
    bs = BeautifulSoup(temp.text, 'lxml')
    bs = str(bs)
    point = bs.find("subscribers")
    start = point
    while bs[start] != '"':
        start -= 1
    end = point - 1
    subscriber = bs[start + 1:end]
    return subscriber


def instagram():
    user = "dipesh_pal17"
    url = 'https://www.instagram.com/' + user
    r = requests.get(url).text

    start = '"edge_followed_by":{"count":'
    end = '},"followed_by_viewer"'

    follower = r[r.find(start)+len(start):r.rfind(end)]

    return follower


def twitter():
    handle = 'Dipesh17Pal'
    temp = requests.get('https://twitter.com/'+handle)
    bs = BeautifulSoup(temp.text, 'lxml')
    try:
        follow_box = bs.find('li', {'class': 'ProfileNav-item ProfileNav-item--followers'})
        followers = follow_box.find('a').find('span', {'class':'ProfileNav-value'})
        twitter_follower = followers.get('data-count')
        return twitter_follower
    except:
        print('Account name not found...')


try:
    youtube_subscriber = youtube()
    print("YouTube Subscriber: ", youtube_subscriber)
except:
    print("You may have some problem with YouTube")

try:
    instagram_follower = instagram()
    print("Instagram Followers: ", instagram_follower)
except:
    print("You may have some problem with Instagram")

try:
    twitter_follower = twitter()
    print("Twitter Follower: ", twitter_follower)
except:
    print("You may have some problem with Twitter")

