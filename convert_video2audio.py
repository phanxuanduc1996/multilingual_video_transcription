import os
import sys
from moviepy.editor import VideoFileClip


def convert_video_to_audio_moviepy(video_file, output_ext="wav"):  # mp3
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""

    filename, ext = os.path.splitext(video_file.split("/")[-1])

    clip = VideoFileClip(video_file)
    if clip.audio:
        # , verbose=False, logger=None
        clip.audio.write_audiofile(f"youtube_audios/{filename}.{output_ext}")


if __name__ == "__main__":
    vf = sys.argv[1]
    if os.path.isfile(vf):
        convert_video_to_audio_moviepy(vf)
    elif os.path.isdir(vf):
        filenames = [os.path.join(vf, filename) for filename in os.listdir(vf)]

        for filename in filenames:
            convert_video_to_audio_moviepy(filename)
    else:
        raise (f"CAN NOT READ FILE PATH...")

