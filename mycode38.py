# 49 exercise 6 solution pending
# 50
# exercise 7
# healthy programmer
# 9am to 5pm
# whater.mp3(3.5 leteres)-Drank-log-every 40 minutes
# eyes.mp3-done every 30 minutes-eydone-log
# physical activity -physical.mp3 ,every 45 minutes -exdone-log
# rules
# use pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stoper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        a=input()
        if a==stoper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt",'a') as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__=="__main__":
    # musiconloop("bewafa.mp3", "stop")
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watersecs=30*60
    exsecs=50*60
    eyesecs=55*60

    while True:
        if time() - init_water > watersecs:
            print("its time to drink water..enter 'drank' to stop the alarm,after drinking the water")
            musiconloop('bewafa.mp3', 'drank')
            init_water=time()
            log_now("drank water at ")


        if time() - init_exercise > exsecs:
            print("its time to stretch your body please do it and enter 'exdone' once u done it")
            musiconloop('bewafa.mp3', 'exdone')
            init_exercise=time()
            log_now("done the exercise at ")


        if time() - init_eyes > eyesecs:
            print("its time to give some rest for ur eyes and enter 'eydone' once u done it ")
            musiconloop('bewafa.mp3', 'eydone')
            init_eyes=time()
            log_now("done the eyes exercise at ")





