# Importing necessary libraries
from tkinter import *
import tkinter.messagebox as mb

import json
import requests

# Fungsi
def extract_lyrics():
	global artist, song
	artist_name = str(artist.get())
	song_name = str(song.get()).lower()
	link = 'https://api.lyrics.ovh/v1/'+artist_name.replace(' ', '%20')+'/'+song_name.replace(' ', '%20')

	req = requests.get(link)
	json_data = json.loads(req.content)

	try:
		lyrics = json_data['lyrics']

		exec("print(lyrics)")

		mb.showinfo('Lyrics printed', f'Lirik lagu yang Anda inginkan telah diekstraksi, dan telah dicetak di terminal perintah Anda.')
	except:
		mb.showerror('No such song found',
		'We were unable to find such a song in our directory. Please recheck the name of the artist and the song, and if it correct, we apologize because we do not have that song available with us.')


# Menginisialisasi windows nya
root = Tk()
root.title("Ekstraktor Lirik Lagu")
root.geometry("600x200")
root.resizable(0, 0)
root.config(bg='CadetBlue')

# Placing the components
Label(root, text='Ekstraktor Lirik Lagu', font=("Roboto", 16, 'bold'), bg='CadetBlue').pack(side=TOP,fill=X)

Label(root, text='Enter the song name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=50)
song = StringVar()
Entry(root, width=40, textvariable=song, font=('Times New Roman', 14)).place(x=200, y=50)

Label(root, text='Enter the artist\'s name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=100)
artist = StringVar()
Entry(root, width=40, textvariable=artist, font=('Times New Roman', 14)).place(x=200, y=100)

Button(root, text='Extract lyrics', font=("Georgia", 10), width=15, command=extract_lyrics).place(x=220, y=150)

# Menyelesaikan windows
root.update()
root.mainloop()