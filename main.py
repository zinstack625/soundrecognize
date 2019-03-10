from time import sleep
import recorder
import player
import prepare


recording = []
samples = 0

(recording, samples) = recorder.record(2)
recording = prepare.prepare(recording)


player.replay(b''.join(recording))
