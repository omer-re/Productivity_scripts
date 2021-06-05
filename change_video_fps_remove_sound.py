import subprocess
import os
in_file=input("Enter input file path: ")
out_file_=input("Enter output file name: ")+".mp4"
out_file=out_file_.replace(" ", "")
fps_rate=(input("Choose FPS parameter: "))
remove_sound=input("Remove sound [Y/N]?: ")
print(in_file,out_file,fps_rate)
if remove_sound=="Y":
    c = 'ffmpeg -y -i "'+in_file+'" -an -r '+fps_rate+' -s 960x540 -c:v libx264 -b:v 3M -strict -2 -movflags faststart '+out_file
elif remove_sound=="N":
    c = 'ffmpeg -y -i "'+in_file+'" -r '+fps_rate+' -s 960x540 -c:v libx264 -b:v 3M -strict -2 -movflags faststart '+out_file
else:
    print("Wrong input")
subprocess.call(c, shell=True)

#ffmpeg -y -i listening_in_class_short.mp4 -an -r 0.5 -s 960x540 -c:v libx264 -b:v 3M -strict -2 -movflags faststart listen_fps1.mp4
