import subprocess

# zapisywanie strumienia do pliku - zmiana parametrow pozniej
subprocess.call([".\\ffmpeg\\bin\\ffmpeg", "-i", "rtsp://admin:DoTestowania@172.20.16.106:554/profile1/media.smp", "-acodec", "copy", "-vcodec", "copy", "test.mp4"], shell=True)
