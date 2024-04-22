from pytube import YouTube
print("HI!! This is a Simple Script to Download a Video From YouTube!!")

# YT video URL
video_url = input("# ")
path=input("PATH: ")
try:
    yt = YouTube(video_url)
    print("title:", yt.title)
    print("views:", yt.views)

    stream = yt.streams.get_highest_resolution()

    stream.download(path)
    print("Done !!")

except Exception as e:
    print(f"An error occurred: {str(e)}")

