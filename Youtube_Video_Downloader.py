from pytube import YouTube

print("HI THERE This is a Simple Script to Download a Video From YouTube!!")

# Enter the YouTube video URL
video_url = input("Enter the video URL: ")

try:
    # Create a YouTube object with the video URL
    yt = YouTube(video_url)

    # Select the highest quality video stream and download it
    stream = yt.streams.get_highest_resolution()
    stream.download()

    print("The Video is Downloaded Successfully !!")

except Exception as e:
    print(f"An error occurred: {str(e)}")
