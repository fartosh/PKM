import subprocess

# zapisywanie strumienia do pliku - zmiana parametrow pozniej
profile = 2
IP = "172.20.16.106"
port = 554
filename = "strzyza"
login = "admin"
password = "DoTestowania"

subprocess.call([".\\ffmpeg\\bin\\ffmpeg", "-i", "rtsp://"+login+":"+password+"@"+IP+":"+port.__str__()+"/profile"+profile.__str__()+"/media.smp", "-acodec", "copy", "-vcodec", "copy", filename+".mp4", "-y"], shell=True)

