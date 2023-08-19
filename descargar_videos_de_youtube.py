import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from pytube import YouTube
from PIL import Image, ImageTk

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("408x721")
        
        self.background_image = Image.open("ajj.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)
        
        self.label = tk.Label(root, text="Ingrese la URL del video:", font=("Helvetica", 12))
        self.label.pack(pady=10)
        
        self.url_entry = tk.Entry(root, font=("Helvetica", 12), width=40)
        self.url_entry.pack(pady=5)
        
        self.download_button = tk.Button(root, text="Descargar", font=("Helvetica", 12), command=self.download_video)
        self.download_button.pack(pady=10)
        
    def download_video(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una URL válida.")
            return
        
        try:
            yt = YouTube(url)
            video_stream = yt.streams.get_highest_resolution()
            
            video_filename = f"{yt.title}.mp4"  # Agregar la extensión .mp4
            
            video_stream.download(filename=video_filename)
            messagebox.showinfo("Éxito", f"El video '{yt.title}' ha sido descargado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al descargar el video:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
