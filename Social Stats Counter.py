from bs4 import BeautifulSoup
import requests


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


def youtube():
    # Twitter
    url = 'https://www.youtube.com/channel/UCGEoRAK92fUk2kY3kSJMR_Q'
    temp = requests.get(url)
    bs = BeautifulSoup(temp.text, 'lxml')
    bs = str(bs)
    point = bs.find("subscribers")
    start = point-6
    end = point
    subscriber = bs[start:end]
    return subscriber


t = twitter()
y = youtube()

print(y)
