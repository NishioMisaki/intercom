import pygame.mixer
import time

def audio():
    #mixerモジュールの初期化
    pygame.mixer.init()
    #音声ファイルの読み込み
    pygame.mixer.music.load("audio.mp3")
    #音声再生、および再生回数の設定
    pygame.mixer.music.play(1)
    time.sleep(3)
    pygame.mixer.music.stop()