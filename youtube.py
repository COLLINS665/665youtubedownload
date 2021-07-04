#first install the latest version of Pytube using pip install pytube
#then import YouTube from pytube

from pytube import YouTube

#declare a variable to hold the video link

vidlink="" #paste Youtube link inside the quotes
video=YouTube(vidlink)
stream=video.streams.get_highest_resolution()
stream.download()
