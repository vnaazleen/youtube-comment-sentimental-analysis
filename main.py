import re  # for pattern matching
import csv

import extractor

def extract_video_id(url):
    '''
        Returns id of the given youtube video url.
    '''

    # youtube video links can be in 2 patterns
    # one including https & one without https
    pattern1  = "^https://www\.youtube\.com/watch\?v=.*$"
    pattern2  = "www\.youtube\.com/watch\?v=.*$"

    # checking if the url matches any of the patterns, then its valid
    if re.match(pattern1, url) or re.match(pattern2, url):
        # if url is valid, extracting the id by splitting at '=', everything after '=' is id
        index = url.find('=')
        video_id = url[index + 1:]
        return video_id
    
    # if video url is invalid, we return None
    return None

def bag_of_words(words):
    return dict([word, True] for word in words)

# Main execution function of Project
if __name__ == '__main__':
    # take url as input from the user 
    youtube_video_url = input("Enter URL of youtube video: ")

    # By default, we are considering ratio as 100
    comments_ratio = 100

    # Extract video id from url
    video_id = extract_video_id(youtube_video_url)

    # if url is invalid, we just print it
    # else we perform sentiment analysis
    if video_id is None:
        print("Invalid URL")
    else:
        print("Video is valid")

        # Extracting the youtube comments
        comments = extractor.get_youtube_comments(video_id=video_id)
        comments = [[comment] for comment in comments]
        fields = ['Comment']

        with open('Comments.csv', 'w') as f:
            write = csv.writer(f)

            write.writerow(fields)
            write.writerows(comments)