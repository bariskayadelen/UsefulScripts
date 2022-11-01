# import youtube_dl
# def run():
#     video_url = input(f"\n Please enter youtube video URL : ")
#     video_info = youtube_dl.YoutubeDL().extract_info(
#         url = video_url,download=False
#     )

#     # Currently 3gp, aac, flv, m4a, mp3, mp4, ogg, wav, webm file extensions are supported
#     filename = f"{video_info['title']}.mp3"
#     options={
#         'format':'bestaudio/best',
#         'keepvideo':False,
#         'outtmpl':filename,
#         'nocheckcertificate':True,
#     }

#     with youtube_dl.YoutubeDL(options) as ydl:
#         ydl.download([video_info['webpage_url']])

#     print("Download complete... {}".format(filename))

# if __name__=='__main__':
#     run()

from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    # ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
    ydl.download(['https://youtu.be/85A0N1EqHbw'])