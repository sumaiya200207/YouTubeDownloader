import yt_dlp
import tkinter as tk
from tkinter import simpledialog, messagebox


root = tk.Tk()
root.withdraw()

url = simpledialog.askstring("Oye", "Enter any youtube url you want to download:")

#url = 'https://youtu.be/rqeCzp4c1Zg?si=dTWHy2gOqGd5IsHb'

ytd_opt = {}

with yt_dlp.YoutubeDL(ytd_opt) as ydl:
    ydl.download(url)


#print("Successfully downloaded")

messagebox.showinfo("Oye", "Successfully downloaded ")