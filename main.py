from time import sleep
import recognizer
import player


recording = []
samples = 0

(recording, samples) = recognizer.recognize(2)
player.replay(b''.join(recording))
sleep(2)
