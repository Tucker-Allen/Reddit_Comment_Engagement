#Imports
import time
import datetime
import pandas as pd

col_names = ['Timestamp', 'Title', 'Created', 'Author', 'Subreddit', 'Score', 'Upvotes', 'Upvote_Ratio', 'Domain', 'Is_Reddit', 'Is_Video',
            'Num_Crossposts', 'Over_18', 'Whitelist_Status', 'Parent_Whitelist_Status', 'Permalink',
            'Thumbnail_Height', 'Thumbnail_Width', 'Selftext_html', 'Num_Comments']

df = pd.DataFrame(columns=col_names)

# Create authorized connection with reddit API
import praw
reddit = praw.Reddit(client_id='y1RZY5qxTYC-3w', client_secret="AxKSfjJJ6ZvV8n79qk3I0lqVIAk", 
                     user_agent='MacBook:GA-NYC Project 3:v1.0 (by /u/PhilPizza)')

read_count = 0
while read_count < 193: 
    response = reddit.front.hot(limit=500) 
    time_now = datetime.datetime.now()
    
    print('On read_count: ' + str(read_count))
    for i in response:
        time_created = i.created_utc
        data_dict = {'Timestamp':time_now, 'Title':i.title, 'Created':datetime.datetime.fromtimestamp(time_created), 'Author':i.author, 
                     'Subreddit':i.subreddit, 'Score':i.score, 'Upvotes':i.ups, 'Upvote_Ratio':i.upvote_ratio, 
                     'Domain':i.domain, 'Is_Reddit':i.is_reddit_media_domain, 'Is_Video':i.is_video, 
                     'Num_Crossposts':i.num_crossposts, 'Over_18':i.over_18, 'Whitelist_Status':i.whitelist_status, 
                     'Parent_Whitelist_Status':i.parent_whitelist_status, 'Permalink':i.permalink, 
                     'Thumbnail_Height':i.thumbnail_height, 'Thumbnail_Width':i.thumbnail_width, 
                     'Selftext_html':i.selftext_html, 'Num_Comments':i.num_comments}
        df = df.append(data_dict, ignore_index=True)    
    read_count += 1
    print('sleeping')
    time.sleep(420) #7 minute sleep, function takes about 8 minutes to run
    # Outputs a csv every 16 read_counts.
    if read_count % 16 == 0:
        print('Saving to file')
        df.to_csv('./Data_'+str(read_count))
print('Done')