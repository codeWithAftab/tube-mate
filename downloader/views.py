from downloader.lyrics import *
from django.shortcuts import render,redirect
import pytube
from django.http import FileResponse, HttpRequest, HttpResponse
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.storage import staticfiles_storage
from tubemate import settings
from downloader.models import History
from downloader.t import get_hall_ticket
from downloader.models import classImages
from downloader.email import emailWithAttach
from downloader.main import get_hall_ticket2022june
# Create your views here.
def home(request):
    return render(request,"home.html")

def videos(request):
    if request.GET["query"]:
        query = request.GET["query"]
        history = History(search=query)
        history.save()
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
        audio = []
        video_streams = yt.streams.filter(progressive=True)
        audio_stream1 = yt.streams.get_by_itag("251")
        audio_stream2 = yt.streams.get_by_itag("250")
        audio.append(audio_stream1)
        audio.append(audio_stream2)
        context = {
            "vid_title":yt.title,
            "thumbnail":yt.thumbnail_url,
            "length":yt.length,
            "views":yt.views,
            "chennel_url":yt.channel_url,
            "vid_streams":video_streams,
            "audio_streams":audio,

            "video_url":video_streams[-1].url,
            "video_id": query,

        }

        return render(request,"download.html",context)
    


def getHallTicket(request):
    if request.method == "POST":
        # print(os.path.curdir)
        # file_path = os.path.join(settings.STATIC_ROOT, 'data/data.xlsx')
        # print(file_path)
        # df = pd.read_excel(file_path)
        # for item, data in df.iterrows():
        #     try:
        #         name = data["Name"].capitalize()
        #         email = data["Email id"]
        #         enrollment = int(data['Enrollment no'])
        #         phone = data['Phone no']
        #         prog = data['Programme']
        #         SUBJECT = f"Hello {name}.This is Your June 2022 Hall ticket card.😊"
        #         image_url = getImage(enrollment,prog)
        #         print(name)
        #         query = classImages.objects.get(enrol_no=enrollment)      
        try:
            name = request.POST["name"]
            enrollment = request.POST["txtEnrNo"]
            prog = request.POST["ddlProgram"]
            hallticket = get_hall_ticket(enrollment,prog)
            query = classImages.objects.filter(enrol_no=enrollment)
            context={
                "hallticket":hallticket
            }
            if not query:
                person = classImages(name=name,enrol_no=enrollment,prog=prog)
                person.save()
            
        
        except Exception as e:
            print(e)

        return HttpResponse(hallticket)

    return render(request,"index.html")

def getHallonMail(request):
    if request.method == "POST":     
        meam = "" 
        message=""
        try:
            name = request.POST["name"]
            enrollment = request.POST["txtEnrNo"]
            email = request.POST["email"]
            prog = request.POST["ddlProgram"]
            SUBJECT = f"Hello {name}.This is Your June 2022 Hall ticket card.😊"
            msg = get_hall_ticket2022june(enrollment,prog)
            print(name)
            query = classImages.objects.filter(enrol_no=enrollment)
            if not query:
                person = classImages(name=name,enrol_no=enrollment,prog=prog,email=email)
                person.save()
            emailWithAttach(email, SUBJECT, body=msg)
            
            meam = "Your Hall ticket Send on Your mail Please check your mail.<br> Thanx For using our service 😊"
        except Exception as e:
            print(e)
            meam = str(e)
        
        message = meam
        return HttpResponse(f"<h1>{message}</h1>")
    return render(request,"getHallonmail.html")

def add_lyrics(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    if request.method == "POST":
        path = "downloader/media/output/"
        deletefiles(path)
        fss = FileSystemStorage()
        print(request.FILES)
        video = request.FILES.get("video_file")
        lrc = request.FILES.get("lyrics_file")
        video_file = fss.save(f"videos/{video.name}", video)
        lyric_file = fss.save(f"lyrics/{lrc.name}", lrc)
        v_url = fss.url(video_file)
        l_url = fss.url(lyric_file)

        lyrics = decode_lyrics(f"downloader{l_url}")
        output_obj = add_lyrics_to_video(lyrics,f"downloader{v_url}")

        save_video(output_obj,f"downloader/media/output/{video.name}")
        try:
            os.remove(f"downloader{v_url}")
            os.remove(f"downloader{l_url}")
        except Exception as e:
            print(e)
        url = fss.url(f"output/{video.name}")

        return render(request,"output.html",{"url":url})

    return render(request,"inputvideo.html")
    

def inputVideo(request):
    return render(request,"inputvideo.html")

def deletefiles(path):
        try:
            files = os.listdir(path)
            for file in files:
                os.remove(path+file)
                print("deleted")
        except Exception as e:
            print(e)