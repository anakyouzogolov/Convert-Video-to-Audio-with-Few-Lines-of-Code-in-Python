
from moviepy.editor import *

# load video file
video_clip = VideoFileClip("song.mkv")

# convert video file to audio file
audio_clip = video_clip.audio

# create mp3 file using write function
audio_clip.write_audiofile("output.mp3")

# close audio and video
audio_clip.close()
video_clip.close()

