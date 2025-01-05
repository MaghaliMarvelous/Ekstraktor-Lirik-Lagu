from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
import json
import requests

# Fungsi utama untuk ekstraksi lirik lagu
def extract_lyrics():
    global artist, song
    artist_name = str(artist.get()).strip()
    song_name = str(song.get()).strip().lower()


    if not artist_name or not song_name:
        mb.showwarning('Input Error', 'Nama artis dan lagu tidak boleh kosong.')
        return

    # Membuat link API yang disesuaikan dengan nama artis dan lagu
    link = f'https://api.lyrics.ovh/v1/{artist_name.replace(" ", "%20")}/{song_name.replace(" ", "%20")}'

    try:
        # Mengirim permintaan ke API
        req = requests.get(link, timeout=10)
        req.raise_for_status()
        json_data = json.loads(req.content)

        
        lyrics = json_data['lyrics']
        display_lyrics(lyrics)

    except requests.exceptions.RequestException as e:
        mb.showerror('Connection Error', f'Terjadi kesalahan koneksi: {e}')
    except KeyError:
        mb.showerror('No such song found',
                     'Kami tidak dapat menemukan lagu tersebut. Mohon periksa kembali nama artis dan lagunya.')

def display_lyrics(lyrics):
    # Membuat windows nya baru untuk menampilkan lirik
    lyrics_window = Toplevel(root)
    lyrics_window.title("Lyrics")
    lyrics_window.geometry("600x400")
    lyrics_window.resizable(0, 0)

    text_area = Text(lyrics_window, wrap=WORD, font=("Times New Roman", 12))
    text_area.insert(END, lyrics)
    text_area.configure(state='disabled')
    text_area.pack(expand=True, fill=BOTH)

    # Menambahkan tombol untuk menyimpan lirik
    save_button = Button(lyrics_window, text="Save Lyrics", command=lambda: save_lyrics_to_file(lyrics), font=("Georgia", 10))
    save_button.pack(pady=10)

def save_lyrics_to_file(lyrics):
    # Menyimpan lirik ke file
    try:
        filename = f"{song.get()} - {artist.get()}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(lyrics)
        mb.showinfo('Saved', f'Lirik berhasil disimpan ke file: {filename}')
    except Exception as e:
        mb.showerror('Error', f'Gagal menyimpan lirik: {e}')

# Menginisialisasi windows utama
root = Tk()
root.title("Ekstraktor Lirik Lagu")
root.geometry("600x250")
root.resizable(0, 0)
root.config(bg='CadetBlue')


Label(root, text='Ekstraktor Lirik Lagu', font=("Roboto", 16, 'bold'), bg='CadetBlue').pack(side=TOP, fill=X, pady=10)

Label(root, text='Enter the song name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=50)
song = StringVar()
Entry(root, width=40, textvariable=song, font=('Times New Roman', 14)).place(x=200, y=50)

Label(root, text='Enter the artist\'s name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=100)
artist = StringVar()
Entry(root, width=40, textvariable=artist, font=('Times New Roman', 14)).place(x=200, y=100)

Button(root, text='Extract lyrics', font=("Georgia", 10), width=15, command=extract_lyrics).place(x=220, y=150)

# Menyelesaikan windows utama
root.update()
root.mainloop()
