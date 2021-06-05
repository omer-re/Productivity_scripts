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
a_v= input("Leaving A=audio or V=video?")
print("Which video file to mute?")
head, tail = os.path.split(input_name)
new_path=str(head+ "/trimmed_" +tail)
#new_name=os.path.join(head+ "/trimmed_" +tail)
#print("ffmpeg -i \"{}\" -ss {} -to {} \"{}\"".format(input_name, start, end, new_path))
if a_v=="v" or a_v=="V":
	print("saving new file to: " +new_path)
	os.system("ffmpeg -i \"{}\"  -c copy -an \"{}\"".format(input_name, new_path))
elif a_v=="a" or a_v=="A":
	tail=str(tail).replace("4","3")
	new_path=str(head +"/"+tail)
	print (new_path)
	print ("ffmpeg -i \"{}\"  -vn \"{}\"".format(input_name, new_path))
	os.system("ffmpeg -i \"{}\"  -vn \"{}\"".format(input_name, new_path))
	
else:
	print("illegal input")
print("\nDone")


#os.system(f"ffmpeg -i \"{name}\" -ss {start} -t {end} -f mp4 \"{new_path}\"" )
#alternative command
#os.system(f"ffmpeg -i {name} -ss {start} -t {end} -c copy start_of_output.mp4")

