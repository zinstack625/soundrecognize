from time import sleep
import recorder
import player


recording = []
samples = 0

(recording, samples) = recorder.record(2)



player.replay(b''.join(recording))
