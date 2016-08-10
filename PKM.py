import subprocess
import sys
from getpass import getpass

# zapisywanie strumienia do pliku - zmiana parametrow pozniej
profile = 2
IP = "172.20.16.106"
port = 554

print "Log in"
login = raw_input("Login: ")
password = raw_input("Password: ")

subprocess.call([".\\ffmpeg\\bin\\ffmpeg", "-i", "rtsp://"+login+":"+password+"@"+IP+":"+port.__str__()+"/profile"+profile.__str__()+"/media.smp", "-acodec", "copy", "-vcodec", "copy", "strzyza.mp4", "-y"], shell=True)

