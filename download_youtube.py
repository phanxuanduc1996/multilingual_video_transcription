# # from __future__ import unicode_literals
# # import youtube_dl

# from pytubefix.cli import on_progress
# from pytubefix import YouTube

# SAVE_PATH = r"videos/"

# # link = "https://www.youtube.com/watch?v=JfVOs4VSpmA&t=3s"
# link = 'http://youtube.com/watch?v=9bZkp7q19f0'




    



# # ------------ OPTION 1 ------------------
# # yt = YouTube(link)
# # yt.streams(progressive=True, file_extension='mp4').order_by(
# #     'resolution').desc().first().download(SAVE_PATH, 'videoFilename', 'mp4')


# # ------------ OPTION 2 ------------------
# # def YTDownload(link):
# #     youTubeObject = YouTube(link)
# #     youTubeObject = youTubeObject.streams.get_highest_resolution()
# #     try:
# #         if youTubeObject is not None:
# #             youTubeObject.download(SAVE_PATH)
# #     except:
# #         print("There has been an error.")

# #     print("All good.")

# # link = input("Enter the YouTube video URL: ")
# # YTDownload(link)


# # --------------- OPTION 3 ----------------
# yt = YouTube(link, on_progress_callback=on_progress)
# print(yt.title)

# ys = yt.streams.get_highest_resolution()
# ys.download()


# # ---------------- OPTION 4 ---------------
# # ydl_opts = {}
# # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
# #     ydl.download([link])


# import requests
# def download_video(url, filename):
#     r = requests.get(url)
    
#     with open(filename, 'wb') as f:
#         f.write(r.content)
# # replace 'url' and 'filename'
# download_video('https://youtu.be/9bZkp7q19f0?si=qY-HLsh9KnhY33Qr', 'video.mp4')


import urllib.request
url_link = 'https://youtu.be/9bZkp7q19f0?si=qY-HLsh9KnhY33Qr'  # replace with your actual video url
filename = 'video_name.mp4'
urllib.request.urlretrieve(url_link, filename)