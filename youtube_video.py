import pytube

video_url = input(f"\n Please enter youtube video URL : ")
yt = pytube.YouTube(video_url)
print("\n Title:", yt.title)
print(" Author:", yt.author)
print(" Published date:", yt.publish_date.strftime("%Y-%m-%d"))
print(" Number of views:", yt.views)
print(" Length of video:", yt.length, "seconds")
# yt.streams.get_highest_resolution().filter(only_audio=True).download()
yt.streams.get_highest_resolution().download()
print("\n Video successfullly downloaded from", video_url, "\n")
