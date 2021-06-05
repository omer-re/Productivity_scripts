import os, glob
 
from tkinter import filedialog
import tkinter as tk
 
root = tk.Tk()
root.filename = filedialog.askopenfilename(initialdir=".", title="Select file", filetypes=(("video files","*.avi *.mp4"), ("all files", "*.*")))
if root.filename == "":
    root.destroy()
print("original file's path: "+root.filename)
input_name = root.filename
root.destroy()
video_mult = input("How much faster?")
audio_frac=(1/float(video_mult))
head, tail = os.path.split(input_name)
new_path=str(head+ "/fast_" +tail)
print(new_path)
#new_name=os.path.join(head+ "/trimmed_" +tail)
print("saving new file to: " +new_path)
#ffmpeg -i input.mp4 -filter_complex "[0:v]setpts=0.625*PTS[v];[0:a]atempo=1.6[a]" -map "[v]" -map "[a]" output.mp4


os.system('ffmpeg -i \"{input_name}\" -filter_complex "[0:v]setpts={audio_frac}*PTS[v];[0:a]atempo={video_mult}[a]" -map "[v]" -map "[a]" \"{new_path}\"')
print("\nDone")

#os.system(f"ffmpeg -i \"{name}\" -ss {start} -t {end} -f mp4 \"{new_path}\"" )
#alternative command
#os.system(f"ffmpeg -i {name} -ss {start} -t {end} -c copy start_of_output.mp4")

