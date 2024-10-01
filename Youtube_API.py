from datetime import datetime,timedelta
from googleapiclient.discovery import build
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
api_key= 'AIzaSyDgebGltkHpIRdZUh9RpzrEhpwCVKzFTgY'
channel_id='UC95LfIzLCj48ZQyKDzVaYnA'
youtube=build('youtube','v3',developerKey=api_key)
#Function to get channel statistics
def get_channel_stats(youtube,channel_id):
     request=youtube.channels().list(
       part='snippet,contentDetails, statistics',id=channel_id)
     response=request.execute()
     data=dict( Channel_name=response['items'][0]['snippet']['title'],
               Subscriber_count= response['items'][0]['statistics']['subscriberCount'],
                Views=response['items'][0]['statistics']['viewCount'],
                Total_videos=response['items'][0]['statistics']['videoCount'],
                 playlist_id= response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
                 )
     #The return output will be given dictionary format:
     return data['playlist_id']#to get playlist id
playlistid=get_channel_stats(youtube,channel_id)
print(playlistid)
#Function to get video_id
def get_video_id(youtube,playlistid):
    request=youtube.playlistItems().list(
          part='contentDetails',
          playlistId=playlistid,
          maxResults=71)
    response= request.execute()
    video_ids=[]
    for i in range(len(response['items'])):
         video_ids.append(response['items'][i]['contentDetails']['videoId'])
    next_page_token=response.get('nextPageToken' )
    more_pages=True
    while more_pages:
         if next_page_token is None:
              more_pages=False
         else:
          request=youtube.playlistItems().list(
          part='contentDetails',
          playlistId=playlistid,
          maxResults=71,
          pageToken=next_page_token)
          response= request.execute()
          for i in range(len(response['items'])):
              video_ids.append(response['items'][i]['contentDetails']['videoId'])
              next_page_token=response.get('nextPageToken' )
    return video_ids
video_ids=get_video_id(youtube,playlistid)#returns list of all videoids
print((video_ids))
def get_video_details(youtube, video_ids):
    all_video_stats = []
    for j in range(0, len(video_ids), 30):
        request = youtube.videos().list(
            part='snippet,statistics', 
            id=','.join(video_ids[j:j+30])  # Adjusting the batch size to 30
        )
        response = request.execute()
        for video in response['items']:
            video_stats = {
                'Title': video['snippet']['title'],
                'published_date': video['snippet']['publishedAt'],
                'Views': video['statistics'].get('viewCount', 0),
                'Likes': video['statistics'].get('likeCount', 0),
                'favcount': video['statistics'].get('favoriteCount', 0)
            }
            all_video_stats.append(video_stats)
    
    return all_video_stats

# Assuming `youtube` is your authenticated YouTube API client and `video_ids` is your list of video IDs
video_details = get_video_details(youtube, video_ids)
print(video_details)
import pandas as pd
video_data = pd.DataFrame(video_details)
video_data.to_excel('videodata.xlsx', index=False)
video_data['Views'] = pd.to_numeric(video_data['Views'], errors='coerce')
top_10_videos =video_data.sort_values(by='Views',ascending=False).head(10)
plt.figure(figsize=(12, 10))
sns.barplot(x='Views', y='Title', data=top_10_videos,palette="mako")
plt.xlabel('Views')
plt.ylabel('Title')
plt.title('Top 10 Videos by Views')
# Adjust the x-axis scale and ticks
plt.tight_layout()
plt.show()
#Boxplot of views likes and comments:
# Convert Views and Likes to numeric values
video_data['Views'] = pd.to_numeric(video_data['Views'], errors='coerce')
video_data['Likes'] = pd.to_numeric(video_data['Likes'], errors='coerce')
video_data['Log_Views'] = np.log1p(video_data['Views'])  # log1p is log(1 + x)
video_data['Log_Likes'] = np.log1p(video_data['Likes'])

# Prepare the data for boxplot
log_likes = video_data['Log_Likes']
log_views = video_data['Log_Views']
labels = ['Log Likes', 'Log Views']

# Plot the boxplot
plt.figure(figsize=(10, 6))
plt.boxplot([log_likes, log_views],tick_labels=labels)

plt.xlabel('Metrics')
plt.ylabel('Log Count')
plt.title('Boxplot of Log-Transformed Views and Likes')
plt.show()


