import requests
import os
import json
import re
import time
from joblib import dump, load
import preprocessor as p
from emoji import demojize
from tqdm import tqdm

# Add twitter api token here
bearer_token = ''

user_search_url = "https://api.twitter.com/2/tweets/search/all"
user_tweet_url = 'https://api.twitter.com/2/users/{}/tweets'

regex_pattern = '^.*((my.*personality|me being|my mbti|am\s)|([iI][\'’\s](am|m\s|got|ve|have|went|used)))+(\s|.\w+.){0,4}#*%s+.*$'


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "hakan"
    return r


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def get_users(pers):
    # istj, intp, intj, infj, enfp, entj, enfj, esfj, estp: (my OR Im OR i'm) istj
    # entp, : (my OR Im OR i'm ) mbti entp 
    # estj: estj -"'s estj"
    # --> estj has tons of hate tweets
    total_users = 0    
    total_requests = 0

    query_base = '{} '.format(pers)
    query_extention = 'lang:en -has:media -is:retweet -has:links -is:reply -"\'s mbti" -"\'s personality"'

    query = query_base + query_extention
    params = {'query': query,
              'tweet.fields': 'author_id',
              'max_results': '100'}
    print('QUERY: ' + query)
    print('REGEX: ' + regex_pattern % pers)
    
    users = {}
    texts = []

    while True:
        json_response = connect_to_endpoint(user_search_url, params)
        total_requests += 1

        for data in json_response['data']: 
            if re.search(regex_pattern % pers, data['text'].lower()):
                users[data['author_id']] = []
                texts.append(data['text'])
                total_users += 1
        
        if 'next_token' in json_response['meta']:
            params['next_token'] = json_response['meta']['next_token']
            time.sleep(2)
        else:
            break
        if total_users > 150 or total_requests > 10:
            break

    print(total_users, total_requests)
    return users
    

def get_user_tweets(user_id):
    
    params = {'max_results': '100'}
    tweets = []

    while True:
        try:
            json_response = connect_to_endpoint(user_tweet_url.format(user_id), params)

            for data in json_response['data']: 
                text = demojize(data['text'])
                text = p.clean(text)
                tweets.append(text)

            if 'next_token' in json_response['meta']:
                params['pagination_token'] = json_response['meta']['next_token']
                time.sleep(2)
            else:
                break
            if len(tweets) >= 500:
                break
        except Exception:
            break

    #print(len(tweets))
    return tweets



if __name__ == "__main__":
    pers_list = ['ESTJ', 'INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 'ISTJ', 'ISFJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP']

    user_ids = {}
    
    for pers in pers_list:
        print(pers)
        users = get_users(pers.lower())
        user_ids[pers] = users
        time.sleep(10)
  
    dump(user_ids, './users')

    user_ids = load('./users')

    print('Getting user tweets')
    for pers in pers_list:
       print(pers)
       for user in tqdm(list(user_ids[pers].keys())):
           tweets = get_user_tweets(user)
           user_ids[pers][user] = tweets


    dump(user_ids, './users')
