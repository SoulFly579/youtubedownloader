
import youtube_dl
from tkinter import ttk
from tkinter import filedialog
from tkinter import * 
from tkinter import messagebox
import os

pencere = Tk()
pencere.title("Youtube Converter Programı")
pencere.geometry("800x600")
uygulama = Frame(pencere)
uygulama.grid()

#File Path
def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=pencere, initialdir=currdir, title='Lütfen İndirme yapılacak konumu seçiniz...')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir

filepath = search_for_file_path()

def DownloadFile():
	choose = ytchoose.get()
	sarki = ytsarki.get()
	if sarki:
		if choose:
			if choose == dowloandchoices [0]:
					messagebox.showinfo("Bilgi", "İndirme işlemi başlamıştır...")
					with youtube_dl.YoutubeDL({
							'outtmpl':filepath + '/%(title)s.%(ext)s',
							'format': 'bestaudio/best',
							'extractaudio' : True,  
							'postprocessors': [{
								'key': 'FFmpegExtractAudio',
								'preferredcodec': 'mp3',
							}], 
							'dump_single_json': 'True',
							'extract_flat' : 'True'}) as ydl:
							ydl.download([sarki])
							messagebox.showinfo("Bilgi", "İndirme işlemi bitmiştir...")
			elif choose == dowloandchoices [1] :
					messagebox.showinfo("Bilgi", "İndirme işlemi başlamıştır...")
					with youtube_dl.YoutubeDL({
							'outtmpl':filepath + '/%(title)s.%(ext)s',
							'dump_single_json': 'True',
							'extract_flat' : 'True',
							'format': '480[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'}) as ydl:
							ydl.download([sarki])
							messagebox.showinfo("Bilgi", "İndirme işlemi bitmiştir...")
		else:
			messagebox.showerror("Hata", "Lütfen format seçimi yapınız.")
	else:
		messagebox.showerror("Hata", "Lütfen link giriniz.")

##link üstü bilgi
metin1 = Label(uygulama,text ="İndirmek istediğiniz dosyanın linkini giriniz...")
metin1.grid(padx=100, pady=25)

##Liink girilecek yer
ytsarki = Entry(uygulama, bd=3, width=50)
ytsarki.grid(padx=100,pady=5)
metin2 = Label(uygulama,text ="İndirmek istediğiniz dosyanın formatını seçiniz...")
metin2.grid(padx=100, pady=25)
## Format Seçimi
dowloandchoices = Listbox(uygulama, width=10, height=2, bd=2 ,selectmode="single")
dowloandchoices = ("Ses","Video")
ytchoose = ttk.Combobox(uygulama,values=dowloandchoices)
ytchoose.grid()

metin3 = Label(uygulama, text='Seçtiğiniz dosya dizini aşağıdaki gibidir.\n\n' + filepath)
metin3.grid(padx=100, pady=25)

## Buton ekleme
button2 = Button(uygulama, text= "İndir" , width=10, height=2, command=DownloadFile)
button2.grid(padx=275, pady=25)

pencere.mainloop()
