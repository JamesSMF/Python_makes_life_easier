import pygame
import pyaudio
import wave
import threading
import time

tone = {49:"C3",
        50:"D3",
        51:"E3",
        52:"F3",
        53:"G3",
        54:"A3",
        55:"B3",
        97:"C4",
        115:"D4",
        100:"E4",
        102:"F4",
        103:"G4",
        104:"A4",
        106:"B4"}

def play(path):
   CHUNK    = 1024
   wf       = wave.open(path, 'rb')    # rb = read binary
   data     = wf.readframes(CHUNK)
   p        = pyaudio.PyAudio()
   FORMAT   = p.get_format_from_width(wf.getsampwidth())
   CHANNELS = wf.getnchannels()
   RATE     = wf.getframerate()

   stream = p.open(format            = FORMAT,
                   channels          = CHANNELS,
                   rate              = RATE,
                   frames_per_buffer = CHUNK,
                   output            = True)

   while len(data)>0:
      stream.write(data)
      data=wf.readframes(CHUNK)


pygame.init()
while True:
   time.sleep(0.05)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
      elif event.type == pygame.KEYDOWN:
         print(tone[event.key])
         path = "/Users/liguangyao/github/python/python3/piano/" + tone[event.key] + ".wav"
         threading.Thread(target=play, args=(path,)).start()
