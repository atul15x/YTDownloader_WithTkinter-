import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import CENTER, LEFT, NW, RIGHT, SW, TOP
from PIL import Image,ImageTk
from pytube import YouTube
from tkinter import filedialog
import os
import time


app = tk.Tk()
app.title("YTDownloader")


app.resizable(False, False)

app.geometry("400x500")

app.config(bg='White')

def filepath():
        global path
        try:
          path = filedialog.askdirectory()
          file.config(text=path,fg='blue')
        except:
          file.config(text="Please Select The Download Location",fg='red')
       

def final():
        
        
        try :
                dwpath = path 
                link = entry1.get()
                format = option.get()
                download_path = dwpath
                
                        
                try :
                  if format == 'MP3(audio)':
                    info  = YouTube(link)
                    title = info.title
                    newtitel = title[0:15]
                    newtitel = newtitel.replace(" ","_")
                    newtitel = newtitel.replace("|","_")
                    newtitel = newtitel.replace(":","_")
                    print(title)
                    audio = info.streams.filter(only_audio=True).first().download(download_path,filename=newtitel)
                    os.rename("{}/{}.mp4".format(dwpath,newtitel),"{}/{}.mp3".format(dwpath,newtitel)) 

                    tk.messagebox.showinfo(title="Mp3", message="Download Complete", )
                
                except:

                    tk.messagebox.showerror(title="Error", message="There is Probleam With This Video",)
                
                try: 

                  if format == '1080p':
                    info  = YouTube(link)
                    title = info.title
                    newtitel = title[0:15]
                    newtitel = newtitel.replace(" ","_")
                    newtitel = newtitel.replace("|","_")
                    newtitel = newtitel.replace(":","_")
                    print(title)
                    video = info.streams.filter(res="1080p",file_extension='webm').first().download(download_path,filename="test")
                    audio = info.streams.filter(only_audio=True).first().download(download_path,filename="test")
                    videopath = "{}/test.webm".format(dwpath)
                    audiopath = "{}/test.mp4".format(dwpath)
                    finalp    = "{}/".format(dwpath)

                    merge = "ffmpeg -i {} -i {} -c copy {}{}.mkv".format(videopath,audiopath,finalp,newtitel)
                    os.system(merge)
                    os.remove(videopath)
                    os.remove(audiopath)

                    tk.messagebox.showinfo(title="1080p", message="Download Complete", )

                except:

                    tk.messagebox.showerror(title="Error", message="This Video Have No 1080p Resolution Video",)

                try:
                 
                  if format == '720p':
                    info  = YouTube(link)
                    title = info.title
                    newtitel = title[0:15]
                    newtitel = newtitel.replace(" ","_")
                    newtitel = newtitel.replace("|","_")
                    newtitel = newtitel.replace(":","_")
                    print(title)
                    video = info.streams.filter(res="720p",file_extension='webm').first().download(download_path,filename="test")
                    audio = info.streams.filter(only_audio=True).first().download(download_path,filename="test")
                    videopath = "{}/test.webm".format(dwpath)
                    audiopath = "{}/test.mp4".format(dwpath)
                    finalp    = "{}/".format(dwpath)

                    merge = "ffmpeg -i {} -i {} -c copy {}{}.mkv".format(videopath,audiopath,finalp,newtitel)
                    os.system(merge)
                    os.remove(videopath)
                    os.remove(audiopath)

                    tk.messagebox.showinfo(title="720p", message="Download Complete", )
                
                except:

                  tk.messagebox.showerror(title="Error", message="This Video Have No 720p Resolution Video",)
        except :
          file.config(text="Please Seletct Download",fg='red')


img = tk.PhotoImage(file="logo/LogoYt.png")
photo = tk.Label(app, image=img,bg='white')
photo.pack(side=TOP,pady=20)

####label
ytlink = tk.Label(app, text='Enter Youtube Link Here:')
ytlink.config(font=('helvetica', 10),bg='white')
ytlink.pack(side=TOP,anchor=NW,padx=30,pady=10)


# ####linkSubmit
entry1 = tk.Entry(app,width=38, font=('Helvetica',12),highlightthickness=1)
entry1.config(highlightbackground = "black",highlightcolor= "black")
entry1.pack(side=TOP)


#####option
ytlink = tk.Label(app, text='Enter Download Option:')
ytlink.config(font=('helvetica', 10),bg='white')
ytlink.pack(side=TOP,anchor=NW,padx=30,pady=10)

# create a combobox
option = tk.StringVar()

months = ('1080p','720p','MP3(audio)')

month_cb = ttk.Combobox(app, textvariable=option,width=29)
month_cb.config(font=('Helvetica',15))
month_cb['values'] = months
month_cb['state'] = 'readonly'  # normal
month_cb.pack( padx=5, pady=5)


#####FilePAth

file = tk.Label(app, text='Enter File Path:')
file.config(font=('helvetica', 10),bg='white')
file.pack(side=TOP,anchor=NW,padx=30,pady=10)



openfilepath = tk.Button(text='Set Download Folder', command=filepath, bg='black', fg='white', font=('helvetica', 9, 'bold'))
openfilepath.pack(side=TOP,anchor=NW,padx=30,)


####Download Button
download = tk.Button(text='Download', command=final, bg='red', fg='white', font=('helvetica', 10, 'bold'))
download.pack(pady=30)





app.mainloop()