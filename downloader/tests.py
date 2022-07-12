import pytube

yt = pytube.Search("suit punjabi")
print(yt.results)
print(yt.results)

for video in yt.results:
    print(video.title)