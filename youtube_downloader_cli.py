from pytube import YouTube

def video_downloader(video_url):
    my_video = YouTube(video_url)
    my_video.streams.get_highest_resolution().download()
    return my_video.title

    #choose video quality
    #specify resolution

try: 
    YouTube_link = input('enter the video link: ')
    print(f'Downloadin your video, please wait.....')
    video = video_downloader(YouTube_link)
    print(f'"{video}" downloaded succesfully')

except: 
    print(f'Download failed')