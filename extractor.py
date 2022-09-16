import sys # for exit function
from itertools import islice
from youtube_comment_downloader import *

def get_youtube_comments(video_id):
    '''
        Returns list of comments for given youtube video with video_id.
    '''

    try:
        print("Downloading Comments for for YouTube video:", video_id)
        count =  0
        comments = []
        for comment in download_comments(video_id):
            comments.append(comment['text'])
            if count >= 200:
                break 
            count += 1
        
        print("Downloaded", count, "comment(s)")
        return comments 
        
    except Exception as e:
        print("Error:", str(e))
        sys.exit(1)

def download_comments(video_id):
    '''
        Helper method, which downloads comments
    '''
    video_url = 'https://www.youtube.com/watch?v=' + video_id
    downloader = YoutubeCommentDownloader()
    comments = downloader.get_comments_from_url(video_url, sort_by=SORT_BY_POPULAR)
    return comments