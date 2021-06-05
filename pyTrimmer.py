import os, glob
 
from tkinter import filedialog
import tkinter as tk
 
root = tk.Tk()
root.filename = filedialog.askopenfilename(initialdir=".", title="Select file", filetypes=(("video files","*.avi *.mp4 *.mp3"), ("all files", "*.*")))
if root.filename == "":
    root.destroy()
print("original file's path: "+root.filename)
input_name = root.filename
root.destroy()
print("Tell me where to start and end...")
start = input("Start (HH:MM:SS):")
end = input("End (HH:MM:SS):")
head, tail = os.path.split(input_name)
new_path=str(head+ "/trimmed_" +tail)
#new_name=os.path.join(head+ "/trimmed_" +tail)
print("saving new file to: " +new_path)
print("ffmpeg -i \"{}\" -ss {} -to {} \"{}\"".format(input_name, start, end, new_path))
os.system("ffmpeg -i \"{}\" -ss {} -to {} \"{}\"".format(input_name, start, end, new_path))
print("\nDone")

#os.system(f"ffmpeg -i \"{name}\" -ss {start} -t {end} -f mp4 \"{new_path}\"" )
#alternative command
#os.system(f"ffmpeg -i {name} -ss {start} -t {end} -c copy start_of_output.mp4")

# trimming audio
#ffmpeg -i Yael.mp3 -ss 00:09:20 -t 00:02:00 -c:a copy Yael_trim.mp3