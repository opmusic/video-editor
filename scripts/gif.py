'''
This function gives you the possibility to 
create a gif from a video, by giving a start and end time.

TODO Change gif size within commandline instead of source code.
'''

import moviepy.editor as mp
import os

def time_symetrize(video_clip):
    return mp.concatenate([video_clip, video_clip.fx(mp.vfx.time_mirror)])

def create_gif():
    # Give user the option to create a gif out of the video.

    file_path = input('Enter path to file: ')
    os.system('cls')

    # Used to rename the new file to .gif
    index = file_path.find('.mp4')

    start_time = int(input('Enter start time: '))
    end_time = int(input('Enter end time: '))

    video = (mp.VideoFileClip(file_path)
            .subclip(start_time, end_time)
            .resize(1)
            .fx(time_symetrize))  # Returns the clip played forward then backwards

    new_filename = file_path[:index] + '.gif'
    final_gif = mp.CompositeVideoClip([video])

    final_gif.write_gif('./assets/gifs/' + new_filename)
    