print("Hackers United Youtube Video Downloader")
print("Contact Us: https://hackersunited.ml")
print("Created By Teniola Ayodele")

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")
    

        

#download video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")
            
root = Tk()
root.title("Hackers United Youtube Video Downloader")
root.geometry("400x400") #set window
root.columnconfigure(0,weight=1)#set all content in center

#Title Label
titleLabel = Label(root,text="Hackers United YT Video Downloader",font=("jost",15,"bold"))
titleLabel.grid()

#Tit Label
titLabel = Label(root,text="Contact Us: https://hackersunited.ml",font=("jost",15,"bold"))
titLabel.grid()

#Titl Label
titlLabel = Label(root,text="Created By Teniola Ayodele",font=("jost",15,"bold"))
titlLabel.grid()

#Ytd Link Label
ytdLabel = Label(root,text="Enter the URL of the Video",font=("jost",15))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
ytdError = Label(root,text="Please Paste the YouTube Video Link Above",fg="red",font=("jost",11,"italic"))
ytdError.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video File",font=("jost",15,"bold"))
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error Msg location
locationError = Label(root,text="Please Choose a Path",fg="red",font=("jost",10))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#download btn
downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

#developer Label
developerlabel = Label(root,text="Owned by Hackers United",font=("jost,15"))
developerlabel.grid()

#develope Label
developelabel = Label(root,text="For Educational Purposes",font=("arial,15"))
developelabel.grid()
root.mainloop()
