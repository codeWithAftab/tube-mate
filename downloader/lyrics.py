import moviepy.editor as mpe
import os

import random
def add_lyrics_to_video(lyrics,inputfile):
    video = mpe.VideoFileClip(inputfile)
    video.duration
    text_clips = [video]
    screensize = (1200,250)
    fonts = mpe.TextClip.list('font')
    print(fonts)
    colors = mpe.TextClip.list('color')
    fonts = ["Showcard-Gothic"]
    w, h = video.size

    positions = [(10,10)]
    posx="center"
    posy = 10
    for lyric in lyrics:
        font = random.choice(fonts)
        color = random.choice(colors)
        txt_clip = mpe.TextClip(lyric["text"],fontsize=100,size=screensize,method="caption",kerning=3,interline=-1,font=font,color="white")\
            .set_start(lyric["seconds"])\
            .set_end(lyric["s_end"])\
                .set_position((posx,posy))
        
        posy+=70
        if posy > 500:
            posy = 10
        if video.duration < lyric["seconds"]:
            break
        # txt_mov = txt_clip.set_pos(lambda t:(max(w / 5, int(-0.2 * w * t)),  
        #                     max(h * 4 / 10, int(10 * t))))

        text_clips.append(txt_clip)
    
    return mpe.CompositeVideoClip(text_clips)
    
def getNextTime(i,items):
    t_stamp = str(items[i+1]).split("]")[0].split("[")[-1]
    song_time_list = t_stamp.split(":")
    t_min = int(song_time_list[0])
    t_seconds = float(song_time_list[-1])
    t_seconds = float("{:.2f}".format((t_min*60)+t_seconds))
    return t_seconds

def save_video(file,path):
    file.write_videofile(path,fps=25)
    return path

def decode_lyrics(file):
    lyrical_texts = []

    with open(file,"rb") as f:
        lyrics = f.read().splitlines()
    
    for i,l in enumerate(lyrics):
        try:
            if i+1 != len(lyrics):
                next_time_stamp = getNextTime(i,lyrics)
            else:
                next_time_stamp = 0

            t_stamp = str(l).split("]")[0].split("[")[-1]
            song_time_list = t_stamp.split(":")
            t_min = int(song_time_list[0])
            t_seconds = float(song_time_list[-1])
            t_seconds = float("{:.2f}".format((t_min*60)+t_seconds))
            l_text = str(l).split("]")[-1].replace("'","")
            print(l_text)
            lyrics_obj = {
                "duration":next_time_stamp-(t_seconds+0.5),
                "s_end":next_time_stamp,
                "seconds":t_seconds,
                "text":l_text
            }

            lyrical_texts.append(lyrics_obj)
        except Exception as e:
            print(e)

    return lyrical_texts

if __name__=="__main__":
    lyricsFile = input("Enter the lyrics file name (with extension): ")
    filename = input("Enter the video file name (with extension): ")
    lyrics = decode_lyrics(os.path.join("lyrics files",lyricsFile))
    f = add_lyrics(lyrics,f"video/{filename}")
    save_video(f,"output","p.mp4")