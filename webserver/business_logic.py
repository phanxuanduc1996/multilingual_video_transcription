import os
import tempfile
from pprint import pprint
import whisper
from pytube import YouTube
from utils import is_youtube_url


def transcribe_video_orchestrator(url: str,  model_name: str):
    if is_youtube_url(url):
        video = download_youtube_video(url)
    else:
        if os.path.exists(url):
            video = {}
            video_name = url.split("/")[-1]
            video_thumbnail = os.path.splitext(video_name)[0]
            video_path = os.path.abspath(url)

            video = {"name": video_name,
                     "thumbnail": video_thumbnail, "path": video_path}

    transcription = transcribe(video, model_name)
    return transcription


def transcribe_video_streaming(audio, model_name):
    transcription = transcribe_streaming(audio, model_name)
    return transcription


def transcribe_streaming(audio, model_name="medium"):
    print("Transcribing streaming...")
    print("Using model:", model_name)

    model = whisper.load_model(model_name)
    result = model.transcribe(audio, )

    pprint(result)
    return result["text"]


def transcribe(video: dict, model_name="medium"):
    print("Transcribing...", video['name'])
    print("Using model:", model_name)

    model = whisper.load_model(model_name)
    result = model.transcribe(video['path'], )

    pprint(result)
    return result["text"]


def download_youtube_video(youtube_url: str) -> dict:
    print("Processing : " + youtube_url)
    directory = tempfile.gettempdir()
    # pdb.set_trace()

    yt = YouTube(youtube_url)

    file_path = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(directory)
    print("VIDEO NAME " + yt._title)
    print("Download complete:" + file_path)
    return {"name": yt._title, "thumbnail": yt.thumbnail_url, "path": file_path}


def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")
