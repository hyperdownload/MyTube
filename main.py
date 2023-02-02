#Compiler command python C:\Users\yamir\AppData\Local\Programs\Python\Python310\Scripts\pyinstaller.exe --onefile --noconsole --uac-admin  --icon=icon.ico main.py
import sys
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pytube
from pytube import Playlist, YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import os
import threading
path=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
window = tk.Tk()
playlistcom=tk.IntVar()
only_audio=tk.IntVar()
def single_link():
    global path
    checkbox.configure(state=tk.DISABLED)
    only_audio_check.configure(state=tk.DISABLED)
    download_lower_button.configure(state=tk.DISABLED)
    label_status.configure(text=f"Descargando, porfavor espere...",bg="gray")
    if only_audio.get()==0:
        if playlistcom.get()==0:
            try:
                link_get=single.get()
                link=YouTube(link_get)
                yt_link=link.title
                single.delete(0, END)
                lower_label_info.configure(text=f"Titulo del video:{yt_link}\n"
                                           f"Desc:{link.description}", anchor="nw")
                ruta_fin = link.streams.get_highest_resolution().download(path) 
                label_status.configure(text="Descarga realizada con exito!",bg="gray")
            except Exception:
                messagebox.showinfo(message="Error al descargar", title="Error!")
                label_status.configure(text="Descarga fallida!",bg="gray")            
        if playlistcom.get()==1:
            try:
                count=0
                playlist = Playlist(single.get())
                cant=len(playlist.video_urls)
                single.delete(0, END)
                for video in playlist.videos:
                    lower_label_info.configure(text=f"Titulo del video:{video.title}\n"
                                           f"Desc:{video.description}", anchor="nw")
                    count+=1
                    ruta_fin = video.streams.get_highest_resolution().first().download(path)        
                    bar=cant*count/100
                    label_status.configure(text=f"{bar}%  Descargado",bg="gray")
                label_status.configure(text="Descarga realizada con exito!",bg="gray")
            except Exception:
                messagebox.showinfo(message="Error al descargar", title="Error!")
                label_status.configure(text="Descarga fallida!",bg="gray")   
    if only_audio.get()==1:
        if playlistcom.get()==0:
            try:
                link_get=single.get()
                link=YouTube(link_get)
                yt_link=link.title
                single.delete(0, END)
                lower_label_info.configure(text=f"Titulo del video:{yt_link}\n"
                                           f"Desc:{link.description}")
                ruta_fin = link.streams.get_audio_only().download(path)
                audioclip = AudioFileClip(ruta_fin)                
                audioclip.write_audiofile(audioclip.filename.replace('.mp4', '.mp3'))
                os.remove(audioclip.filename)
                label_status.configure(text="Descarga realizada con exito!",bg="gray")
            except Exception:
                messagebox.showinfo(message="Error al descargar", title="Error!")
                label_status.configure(text="Descarga fallida!",bg="gray")   
        if playlistcom.get()==1:
            try:
                count=0
                playlist = Playlist(single.get())
                cant=len(playlist.video_urls)
                single.delete(0, END)
                for audio in playlist.videos:
                    lower_label_info.configure(text=f"Titulo del video:{audio.title}\n"
                                           f"Desc:{audio.description}", anchor="nw")
                    count+=1
                    ruta_fin = audio.streams.get_audio_only().download(path)
                    audioclip = AudioFileClip(ruta_fin)                
                    audioclip.write_audiofile(audioclip.filename.replace('.mp4', '.mp3'))
                    os.remove(audioclip.filename)
                    bar=cant*count/100
                    label_status.configure(text=f"{bar}%  Descargado",bg="gray")
                label_status.configure(text="Descarga realizada con exito!",bg="gray")
            except Exception:
                messagebox.showinfo(message="Error al descargar", title="Error!")
                label_status.configure(text="Descarga fallida!",bg="gray")   
    single.delete(0, END)
    checkbox.configure(state=tk.NORMAL)
    only_audio_check.configure(state=tk.NORMAL)
    download_lower_button.configure(state=tk.NORMAL)
def single_link_call():
    threading.Thread(target=single_link).start()
#Widgets
window.title("MyTube")
window.geometry("640x200")
window.iconbitmap(sys.executable)
single = tk.Entry(window,width=50)
single.place(x=25, y=40)
lower_label_info = Label(window, text="")
lower_label_info.place(x=160, y=80)
download_lower_button = tk.Button(text="Descargar", command=single_link_call)
download_lower_button.place(x=25, y=120)
checkbox = ttk.Checkbutton(text="Es una playlist", variable=playlistcom)
checkbox.place(x=25, y=70)
only_audio_check = ttk.Checkbutton(text="Solo audio", variable=only_audio)
only_audio_check.place(x=25, y=90)
label_status=Label(window, text="")
label_status.place(x=25, y=150)
window.mainloop()