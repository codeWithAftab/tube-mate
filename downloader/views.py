from pkgutil import ImpImporter
from django.shortcuts import render,redirect
import pytube
from django.http import FileResponse

from downloader.models import History

# Create your views here.
def home(request):
    return render(request,"home.html")

def videos(request):
    if request.GET["query"]:
        query = request.GET["query"]
        history = History(search=query)
        history.save()
        print(query)
        yt = pytube.Search(query)
        print(yt.results)
        result = yt.results
        context = {
            "results": result,

        }
        return render(request,"videos.html",context)
    return render(request,"videos.html")

def download(request):
    if request.method == "POST":
        pass
        # q = json.loads(request.POST["vid_data"])
        
        # return FileResponse(open(pytube.YouTube(q["video_id"]).streams.get_by_resolution(q["res"]).download(skip_existing=True),'rb'))
    else:
        query = "https://www.youtube.com/watch?v="
        video_id = request.GET["video_id"]
        query = query+video_id
        yt = pytube.YouTube(query)
        streams = yt.streams.filter(progressive=True)
        for stream in streams:
            print(stream)

        context = {
            "vid_title":yt.title,
            "thumbnail":yt.thumbnail_url,
            "length":yt.length,
            "views":yt.views,
            "chennel_url":yt.channel_url,
            "streams":streams,
            "video_url":streams[-1].url,
            "video_id": query
        }

        return render(request,"download.html",context)
    
    # return FileResponse(open(YouTube(url).streams.first().download(skip_existing=True),'rb'))