from django.core.exceptions import ValidationError
from moviepy.editor import VideoFileClip

def validate_video_size(value):
    video_size = value.size


    if video_size > 1073741824: #(10 GB = 1073741824 bytes)
        raise ValidationError("Can't upload more than 10GB")
    else:
        return value


# def validate_length(file):
#     #take the filepath of the video
#     video = VideoFileClip("media/"+file)

#     #check if the length of the video is greater than 600 seconds (10 minutes)
#     #if it is, then raise the error
#     if video.duration > 600:
#         raise ValidationError("Video must have less than 10 minutes of length")
#     else:
#         return True