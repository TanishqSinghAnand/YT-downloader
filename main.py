from pytube import YouTube

link = input("Pls enter your YouTube URL : " )
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

print("Enter the desired option for format of video")
dn_option = int(input("Enter the option : "))

dn_video = videos[dn_option]
dn_video.download()

print("Downloaded Successfully!")